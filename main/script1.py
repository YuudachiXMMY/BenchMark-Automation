import win32api
import win32con
import win32gui
from ctypes import *
import time
from win32 import win32 as w

# def s1():
#     w.mouse_click(500,280)
#     str1 = 'python'
#     w.key_input(str1)
#     w.mouse_click(1000,280)

import win32file, win32api, win32con
import os

# A very simple demo - note that this does no more than you can do with
# builtin Python file objects, so for something as simple as this, you
# generally *should* use builtin Python objects.  Only use win32file etc
# when you need win32 specific features not available in Python.
def SimpleFileDemo():
    testName = os.path.join( "C:/Users/Navi/Desktop/BenchMark-Automation/", "win32file_demo_test_file.txt")
    # testName = os.path.join( win32api.GetTempPath(), "win32file_demo_test_file")
    print(testName)
    if os.path.exists(testName): os.unlink(testName)
    # Open the file for writing.
    handle = win32file.CreateFile(testName,
                                  win32file.GENERIC_WRITE,
                                  0,
                                  None,
                                  win32con.CREATE_NEW,
                                  0,
                                  None)
    test_data = "Hello\0there".encode("ascii")
    win32file.WriteFile(handle, test_data)
    handle.Close()
    # Open it for reading.
    handle = win32file.CreateFile(testName, win32file.GENERIC_READ, 0, None, win32con.OPEN_EXISTING, 0, None)
    rc, data = win32file.ReadFile(handle, 1024)
    handle.Close() #此处也可使用win32file.CloseHandle(handle)来关闭句柄
    if data == test_data:
        print("Successfully wrote and read a file")
    else:
        raise Exception("Got different data back???")
    os.unlink(testName)

if __name__=='__main__':
    SimpleFileDemo()