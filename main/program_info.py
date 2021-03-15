from main import _LANGUAGE
import os

WORKING_DIRECTORY = os.getcwd()
_TAB = "    "
_LANGUAGE = 0

def showEN():
    print("Due to time stress, didn't finish the localization of this section for English")
    print("You should and must choose Chinese Version to see the vital setup guide. Please utilize Google Translate :)")

def showCN():
    print("\n"+"*"*100)
    print("！！！！！ 此程序仅供AMD内部使用 ！！！！！")
    print(""+"*"*100)

    print("\n！！ 请确保电脑系统的分辨率环境为2k ！！\n")

    print("运行游戏前请确保:")
    print(_TAB+"1. 游戏已安装在下述路径内；")
    print(_TAB+"2. 游戏完整且可以正常运行；")
    print(_TAB+"3. 运行游戏时不会弹出steam云同步等其他内容，并且居中会直接跳出游戏启动器。\n")

    print("请确保运行过程中:")
    print(_TAB+"1. 不要触碰电脑的鼠标和键盘；")
    print(_TAB+"2. Steam不会被顶号；")
    print(_TAB+"4. 游戏内不会弹出更新内容等通知消息。\n")

    print("内测功能:")
    print(_TAB+"1. 目前可选择自动运行四款游戏的Benchmark；")
    print(_TAB+"2. 可选择每个游戏运行多少次；")
    print(_TAB+"3. 目前支持的部分游戏会跑1080p和2k。\n")
    print(_TAB+"4. 支持在data.json内保存脚本设置。\n")

    print("【必看】运行此Automation脚本前需做：")
    print(_TAB+"1. 必须先使用Notepad打开data.json，修改内部的本机文档路径和Steam路径")
    print(_TAB+"2. 系统环境的分辨率为2k 144hz")
    print(_TAB+"3. 每次运行【文明6】时，必须将初始设置为2k全屏模式，游戏性能可自行设置(后续追加优化)；\n")

    print("【自定义】")
    print(_TAB+"1. 修改本地文档、Steam路径和其他benchmark路径:")
    print(_TAB+_TAB+"a.先到路径： %s"%WORKING_DIRECTORY)
    print(_TAB+_TAB+"b.用Notepad打开 \'data.json\'")
    print(_TAB+_TAB+"** 注意！路径斜杠请使用双斜杠：\'//\'代替\'\\\'")

def initLanguage(language):
    '''
    Set the Language as a Global Variable
    '''
    global _LANGUAGE
    _LANGUAGE = language

def main(lan):
    '''
    Show program information of this automation scripts
    '''

    # Init Program Language
    initLanguage(lan)

    if _LANGUAGE == 0:
        showEN()
    elif _LANGUAGE == 1:
        showCN()
    else:
        print("Something goes wrong")