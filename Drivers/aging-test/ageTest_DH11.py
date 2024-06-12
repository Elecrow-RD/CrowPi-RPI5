#!coding=UTF-8

import CrowpiAllModule as pi
import threading
import time
import atexit
import os

#
#   程序退出时自动执行
#
@atexit.register 
def exit():
    print("所有模块已经退出!")
    

#输出类
def outputTest():
    
    #DH11温湿度
    th_DH11 = threading.Thread(target = pi.dh11)
    th_DH11.start()

def CloseAll():
    pi.g_exit = True
    print("正在关闭所有模块！")
    os.system("sudo bash kill.sh")
    



try:
    if __name__ == "__main__":
        outputTest()

except KeyboardInterrupt:
    pi.g_exit = True
