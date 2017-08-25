from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
class Email:
    def __init__(self,user,pwd,smtp,port,to):
        self._user = user
        self._pwd = pwd
        self._smtp = smtp
        self._port = port
        self._to=to

    def createSQLMsg(self, subject,content,filepath,filename):
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = self._user
        msg["To"] = self._to

        # 邮件正文是MIMEText:
        msg.attach(MIMEText(content, 'plain', 'utf-8'))

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open(filepath, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('text', 'sql', filename=filename+'.sql')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename=filename+'.sql')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)
            return msg

    def createPlainMsg(self, subject,content):
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self._user
        msg['To'] = self._to
        msg['Subject'] = Header(subject, 'utf-8').encode()
        return msg

    def sent(self,msg):
        try:
            s = smtplib.SMTP_SSL(self._smtp, self._port)
            s.login(self._user, self._pwd)
            s.sendmail(self._user, self._to, msg.as_string())
        except smtplib.SMTPException as e:
            print("Falied,%s" % e)
        finally:
            s.quit()



# 应用示例
# email=Email("254449149@qq.com","ufmsdjuhkgdxbibh","smtp.qq.com",465,"254449149@qq.com")
# # msg=email.createSQLMsg("251服务器sql备份","251上的mysql备份","d:/jyghc.sql","jyghc.sql")
# msg=email.createPlainMsg("mysql备份失败","失败")
# email.sent(msg)