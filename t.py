import datetime, time
import re, os
import win32api, win32gui, win32con
import lib.VK_CODE as VK_CODE

WORKING_DIRECTORY = os.getcwd()

def mkDir(logName, dir=''):
    rq = time.strftime('%Y-%m-%d-%H.%M', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/Logs/' + rq
    if dir != '':
            log_path = log_path + dir
    # 判断结果
    if not os.path.exists(log_path):
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(log_path)

mkDir("a", "b")