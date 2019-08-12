## ======= 简单定制=========================
import time

class MyTimer():
    def __init__(self):
        print('未开始计时')
        
    def start(self):
        print('计时开始')
        self.start_time = time.time()

    def stop(self):
        print('计时结束')
        self.stop_time = time.time()
        self.PassTime = self.stop_time - self.start_time

    def __str__(self):
        return '一共运行了' + str('%.2f' % self.PassTime) + '秒...'

    __repr__ = __str__
