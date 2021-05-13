import os
import subprocess
import uiautomation as auto
import time

#打开计算器进程
#定位窗口
wc=auto.PaneControl(searchDepth=1,Name="Shadow of the Tomb Raider")
#设置为顶层
wc.SetTopmost(True)
print(a)
# wc.WindowControl(foundIndex=3, ControlType='Image(50006)', Name='Property does not exist')
# wc.ButtonControl(Name='7').Click()
# wc.ButtonControl(Name='加').Click()
# wc.ButtonControl(Name='5').Click()
# wc.ButtonControl(Name='等于').Click()
# result=wc.TextControl(AutomationId='158')
# print(result.Name)
# if result.Name=="12":
#     print("测试成功")
# else:
#     print("测试失败")
#截图
# wc.CaptureToImage('1.png')
# time.sleep(2)
# os.system("taskkill /F /IM calc.exe")