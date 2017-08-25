# -*- coding:utf-8 -*-
# use sched to timing
import time
import sched
import os

class MySchedClass:
    def __init__(self):
        self.schedule = sched.scheduler(time.time, time.sleep)

    def execute_command(self, inc):
        self.cmd()
        self.schedule.enter(inc, 0, self.execute_command, (inc,))

    def cmd(self):
        pass

    def start(self,inc=600):
        self.schedule.enter(0, 0, self.execute_command, (inc,))
        self.schedule.run()

# # 引用示例
# class ling(MySchedClass):
#     def cmd(self):
#         os.system("ipconfig")
#
# # 调用示例
# s = ling()
# s.start(3)