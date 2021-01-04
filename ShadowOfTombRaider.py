import os
from re import L
import time
import win32gui
import win32api
import win32con

# # 设置appdict
# pyexe = "E:\...\python.exe"
# appdict = {'qq': '"D:\...\QQScLauncher.exe"',
#            'pl/sql': '"E:\...\plsqldev.exe"',
#            'idea': '"E:...\idea64.exe"',
#            'chrome': '"C:\...\chrome.exe"'}
# # qq登录按钮位置，pl/sql取消按钮位置，idea第一个工程的位置
# coorddict = {'qq': [960, 665], 'pl/sql': [1060, 620], 'idea': [700, 245]}
# namedict = {'qq': 'QQ', 'pl/sql': 'Oracle Logon', 'idea': 'Welcome to IntelliJ IDEA'}

# TASK_NAME = "ShadowOfTombRaider"

# # 打开应用并且鼠标点击按钮（获取按钮的像素坐标很麻烦）
# def open_by_grab():
#     pyhd = win32gui.FindWindow(None, pyexe)  # 360会拦截pyexe,可以添加信任或者关闭360
#     # 设置pyexe窗口属性和位置，太大会挡住一些窗口
#     win32gui.SetWindowPos(pyhd, win32con.HWND_TOPMOST, 0, 0, 500, 500, win32con.SWP_SHOWWINDOW)
#     print("py exe 句柄: %s ..." % pyhd)
#     for key in appdict.keys():
#         print("启动 %s ..." % key)
#         os.popen(r'%s' % appdict[key])  # os.system会阻塞
#         time.sleep(3)
#         if key == "chrome":
#             pass
#         else:
#             winhd = win32gui.FindWindow(None, namedict[key])  # 根据窗口名获取句柄
#             while winhd == 0:
#                 print("等待获取%s窗口 ..." % key)
#                 time.sleep(3)
#                 winhd = win32gui.FindWindow(None, namedict[key])
#             print("获取%s窗口成功,开始登录 ..." % key)
#             a, b = coorddict[key]
#             mouse_click(a, b)
#             time.sleep(3)
#     print("完毕 ...")
#     time.sleep(1)
#     win32gui.SendMessage(pyhd, win32con.WM_CLOSE)


# # 模拟鼠标点击
# def mouse_click(a, b):
#     time.sleep(1)
#     win32api.SetCursorPos((a, b))
#     time.sleep(1)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0) # 360会拦截虚拟按键,可以添加信任或者关闭360
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# open_by_grab()
##########################################


from PIL import ImageGrab
import pyautogui as pag

# VK_CODE
VK_CODE = {
    'backspace':0x08,
    'tab':0x09,
    'clear':0x0C,
    'enter':0x0D,
    'shift':0x10,
    'ctrl':0x11,
    'alt':0x12,
    'pause':0x13,
    'caps_lock':0x14,
    'esc':0x1B,
    'spacebar':0x20,
    'page_up':0x21,
    'page_down':0x22,
    'end':0x23,
    'home':0x24,
    'left_arrow':0x25,
    'up_arrow':0x26,
    'right_arrow':0x27,
    'down_arrow':0x28,
    'select':0x29,
    'print':0x2A,
    'execute':0x2B,
    'print_screen':0x2C,
    'ins':0x2D,
    'del':0x2E,
    'help':0x2F,
    '0':0x30,
    '1':0x31,
    '2':0x32,
    '3':0x33,
    '4':0x34,
    '5':0x35,
    '6':0x36,
    '7':0x37,
    '8':0x38,
    '9':0x39,
    'a':0x41,
    'b':0x42,
    'c':0x43,
    'd':0x44,
    'e':0x45,
    'f':0x46,
    'g':0x47,
    'h':0x48,
    'i':0x49,
    'j':0x4A,
    'k':0x4B,
    'l':0x4C,
    'm':0x4D,
    'n':0x4E,
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'r':0x52,
    's':0x53,
    't':0x54,
    'u':0x55,
    'v':0x56,
    'w':0x57,
    'x':0x58,
    'y':0x59,
    'z':0x5A,
    'numpad_0':0x60,
    'numpad_1':0x61,
    'numpad_2':0x62,
    'numpad_3':0x63,
    'numpad_4':0x64,
    'numpad_5':0x65,
    'numpad_6':0x66,
    'numpad_7':0x67,
    'numpad_8':0x68,
    'numpad_9':0x69,
    'multiply_key':0x6A,
    'add_key':0x6B,
    'separator_key':0x6C,
    'subtract_key':0x6D,
    'decimal_key':0x6E,
    'divide_key':0x6F,
    'F1':0x70,
    'F2':0x71,
    'F3':0x72,
    'F4':0x73,
    'F5':0x74,
    'F6':0x75,
    'F7':0x76,
    'F8':0x77,
    'F9':0x78,
    'F10':0x79,
    'F11':0x7A,
    'F12':0x7B,
    'F13':0x7C,
    'F14':0x7D,
    'F15':0x7E,
    'F16':0x7F,
    'F17':0x80,
    'F18':0x81,
    'F19':0x82,
    'F20':0x83,
    'F21':0x84,
    'F22':0x85,
    'F23':0x86,
    'F24':0x87,
    'num_lock':0x90,
    'scroll_lock':0x91,
    'left_shift':0xA0,
    'right_shift ':0xA1,
    'left_control':0xA2,
    'right_control':0xA3,
    'left_menu':0xA4,
    'right_menu':0xA5,
    'browser_back':0xA6,
    'browser_forward':0xA7,
    'browser_refresh':0xA8,
    'browser_stop':0xA9,
    'browser_search':0xAA,
    'browser_favorites':0xAB,
    'browser_start_and_home':0xAC,
    'volume_mute':0xAD,
    'volume_Down':0xAE,
    'volume_up':0xAF,
    'next_track':0xB0,
    'previous_track':0xB1,
    'stop_media':0xB2,
    'play/pause_media':0xB3,
    'start_mail':0xB4,
    'select_media':0xB5,
    'start_application_1':0xB6,
    'start_application_2':0xB7,
    'attn_key':0xF6,
    'crsel_key':0xF7,
    'exsel_key':0xF8,
    'play_key':0xFA,
    'zoom_key':0xFB,
    'clear_key':0xFE,
    '+':0xBB,
    ',':0xBC,
    '-':0xBD,
    '.':0xBE,
    '/':0xBF,
    '`':0xC0,
    ';':0xBA,
    '[':0xDB,
    '\\':0xDC,
    ']':0xDD,
    "'":0xDE}
VK_CODE1 = {
    'A':'a',
    'B':'b',
    'C':'c',
    'D':'d',
    'E':'e',
    'F':'f',
    'G':'g',
    'H':'h',
    'I':'i',
    'J':'j',
    'K':'k',
    'L':'l',
    'M':'m',
    'N':'n',
    'O':'o',
    'P':'p',
    'Q':'q',
    'R':'r',
    'S':'s',
    'T':'t',
    'U':'u',
    'V':'v',
    'W':'w',
    'X':'x',
    'Y':'y',
    'Z':'z',
    ')':'0',
    '!':'1',
    '@':'2',
    '#':'3',
    '$':'4',
    '%':'5',
    '^':'6',
    '&':'7',
    '*':'8',
    '(':'9',
    '=':'+',
    '<':',',
    '_':'-',
    '>':'.',
    '?':'/',
    '~':'`',
    ':':';',
    '{':'[',
    '|':'\\',
    '}':']',
    '"':"'"}

# Global Variable
SCREEN_SIZE = (win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
STEAM_DIRECTORY = "D://SteamLibrary//steamapps//common"
GAME_DIRECTORY = "Shadow of the Tomb Raider"
GAME_EXECUTOR = "SOTTR.exe"
GAME_NAME = "Shadow of the Tomb Raider"

# Helper Methodes
def makeScreenShoot():
    return ImageGrab.grab(bbox=(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]))

def saveScreenShoot(error=''):
    img = makeScreenShoot()
    screenShootName = '{task}_{time}.jpg'.format(task=GAME_NAME, time=time.strftime("%m_%d_%H_%M_%S", time.localtime()))
    if error != '':
        screenShootName = '[%s] '%error + screenShootName
    img.save(screenShootName)
    print("Saved Screen Shoot: %s"%screenShootName)

def findWindow(task):
    print("Waiting for %s window..." % task)
    gameHd = win32gui.FindWindow(None, task)
    tries = 0
    while gameHd == 0:
        time.sleep(3)
        gameHd = win32gui.FindWindow(None, task)
        if tries > 5:
            print("****** failed ******")
            return 0
        tries += 1
    return gameHd

def key_inputs(str_input=''): #自动识别上档键和下档建并输出
    for c in str_input:
        key_input(c)

def key_input(c): #自动识别上档键和下档建并输出
    if c in VK_CODE1:
        win32api.keybd_event(VK_CODE[VK_CODE1[c]],0,0,0) #按键
        win32api.keybd_event(VK_CODE[VK_CODE1[c]],0,win32con.KEYEVENTF_KEYUP,0) #释放按键
        time.sleep(0.1)
    elif c in VK_CODE:
        win32api.keybd_event(VK_CODE[c],0,0,0)#按键
        win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0) #释放按键
        time.sleep(0.1)

def key_enter():
    win32api.keybd_event(VK_CODE["enter"],0,0,0) #按下shift键
    win32api.keybd_event(VK_CODE["enter"],0,win32con.KEYEVENTF_KEYUP,0)#按下shift键
    time.sleep(0.1)

# STEAM_DIRECTORY = input("Please input your Steam Directory:")
def main():

    # startGame = win32api.ShellExecute(1, 'open', r'{STEAM_DIRECTORY}//{GAME_DIRECTORY}//{GAME_EXECUTOR}'.format(STEAM_DIRECTORY=STEAM_DIRECTORY, GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR), '', '', 1)
    # if not startGame:
    #     return 0

    # time.sleep(10)

    # tries = 0
    # while findWindow(GAME_NAME):
    #     time.sleep(3)
    #     key_enter()

    #     gameHD = findWindow("%s v1.0 build 298.0_64"%GAME_NAME)
    #     if gameHD:
    #         tries = 0
    #         print("Success!!")
    #         break
    #     elif tries > 5:
    #         saveScreenShoot("OpenFailed")
    #         print("****** Failed to open Game!!! Process stopped ******")
    #         return 0
    #     tries += 1

    # print("Waiting...")
    # # wait for game start
    # time.sleep(25)
    gameHD = findWindow("%s v1.0 build 298.0_64"%GAME_NAME)
    win32gui.SetForegroundWindow(gameHD)
    time.sleep(5)



    # pag.press('s')

    win32api.PostMessage()
    time.sleep(1)
    pag.press('s')
    time.sleep(1)
    pag.press('s')
    time.sleep(1)
    pag.press('enter')
    time.sleep(2)
    pag.press('s')
    time.sleep(1)
    pag.press('s')
    time.sleep(1)
    pag.press('s')
    time.sleep(1)
    pag.press('enter')
    time.sleep(2)
    pag.press('r')

    # # Start Benchmark
    # key_input("s")
    # time.sleep(1)
    # key_input("s")
    # time.sleep(1)
    # key_input("s")
    # time.sleep(1)
    # key_input("enter")
    # time.sleep(2)
    # key_input("sr")
    # time.sleep(1)
    # key_input("s")
    # time.sleep(1)
    # key_input("s")
    # time.sleep(1)
    # key_input("enter")
    # time.sleep(2)
    # key_input("R")
    # time.sleep(2)

main()