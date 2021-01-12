import os, psutil
import re
from re import L
import time
import datetime
import win32gui
import win32api
import win32con
from PIL import ImageGrab
# import pyautogui as pag

## VK_CODE
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
WORKING_DIRECTORY = os.getcwd()
SCREEN_SIZE = (win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
GAME_DIRECTORY = "Shadow of the Tomb Raider"
GAME_EXECUTOR = "SOTTR.exe"
GAME_NAME = "Shadow of the Tomb Raider"
CONFIG_SETTINGS = ["config_settings/Shadow_of_the_Tomb_Raider_2k_ultra.reg", "config_settings/Shadow_of_the_Tomb_Raider_1080p_ultra.reg"]

# Helper Methodes
def makeScreenShoot():
    return ImageGrab.grab(bbox=(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]))

def saveScreenShoot(error=''):
    '''
    This function saves screenshoots to the "errors" folder
    '''
    img = makeScreenShoot()
    screenShootName = '{task}_{time}.jpg'.format(task=GAME_NAME, time=time.strftime("%m_%d_%H_%M_%S", time.localtime()))
    if error != '':
        screenShootName = '[%s] '%error + screenShootName
    img.save("errors/%s"%screenShootName)
    print("Saved Screen Shoot: %s"%screenShootName)

def findWindow(task):
    '''
    Find a window with 5 tries, each tries have a waiting time of 3 sec.
    - return 0, if can't find the window and save a screenshoot
    - return the window's HD, if succeed in finding the window
    '''
    print("Waiting for %s window..." % task)
    gameHd = win32gui.FindWindow(None, task)
    tries = 0
    while gameHd == 0:
        time.sleep(3)
        gameHd = win32gui.FindWindow(None, task)
        if tries > 5:
            saveScreenShoot("FindWindowFailed")
            print("****** failed ******")
            return 0
        tries += 1
    return gameHd

def key_inputs(str_input=''):
    ''' NOT BE USED SO FAR
    Past function to do a series of keyboard actions.
    # 自动识别上档键和下档建并输出
    '''
    for c in str_input:
        key_input(c)

def key_input(c):
    ''' NOT BE USED SO FAR
    Past function to do a keyboard actions.
    # 自动识别上档键和下档建并输出
    '''
    if c in VK_CODE1:
        win32api.keybd_event(VK_CODE[VK_CODE1[c]],0,0,0) #按键
        win32api.keybd_event(VK_CODE[VK_CODE1[c]],0,win32con.KEYEVENTF_KEYUP,0) #释放按键
        time.sleep(0.1)
    elif c in VK_CODE:
        win32api.keybd_event(VK_CODE[c],0,0,0)#按键
        win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0) #释放按键
        time.sleep(0.1)

def key_enter():
    ''' NOT BE USED SO FAR
    Past function to press shift key.
    '''
    win32api.keybd_event(VK_CODE["enter"],0,0,0) # 按下shift键
    win32api.keybd_event(VK_CODE["enter"],0,win32con.KEYEVENTF_KEYUP,0) # 按下shift键
    time.sleep(0.1)

def searchFile(pathname, filename):
    '''
    Search for a file
    - return the matched file name
    # 参数1要搜索的路径，参数2要搜索的文件名，可以是正则表代式
    '''
    matchedFile =[]
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if re.match(filename,file):
                fname = os.path.abspath(os.path.join(root,file))
                #print(fname)
                matchedFile.append(fname)
    return matchedFile

def searchLog(DOCUMENT_ROOT, starting_time):
    f = []
    c = starting_time
    while(c < datetime.datetime.now()):
        c = c + datetime.timedelta(minutes=1)
        cur_time = ( c ).strftime("%Y-%m-%d_%H.%M")
        res = searchFile("{DOCUMENT_ROOT}//{GAME_NAME}//".format(DOCUMENT_ROOT=DOCUMENT_ROOT, GAME_NAME=GAME_NAME), "SOTTR_X_%s.*.txt"%(cur_time))
        if res:
            f.extend(res)
            return f
    return f

def findGameVersion(DOCUMENT_ROOT):
    '''
    Seach for Tomb Raider's version, in the .log file of the game file in\
    system document folder.
    - return 0, if failed to define the game version
    - return game version, if succeed
    '''
    reg = r'v\d+.\d+ build \d+.\d+_\d+'
    tar_f = DOCUMENT_ROOT + "//%s.log"%GAME_NAME
    with open(tar_f) as f:
        for line in f:
            if re.search(reg, line):
                return re.search(reg, line).group()
    return 0

def press_s():
    '''
    Execute s key, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/s.exe'%WORKING_DIRECTORY, '', '', 1)

def press_enter():
    '''
    Execute enter key, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/enter.exe'%WORKING_DIRECTORY, '', '', 1)

def press_r():
    '''
    Execute r key, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/r.exe'%WORKING_DIRECTORY, '', '', 1)

def press_w():
    '''
    Execute w key, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/w.exe'%WORKING_DIRECTORY, '', '', 1)

def resetMouse():
    '''
    Reset the mouse position to top-left, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/reset_mouse.exe'%WORKING_DIRECTORY, '', '', 1)

def reactWhole_2k():
    '''
    Apply mouse action to get to the graphic screen, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/full_2k.exe'%WORKING_DIRECTORY, '', '', 1)

def reactWhole_1080():
    '''
    Apply mouse action to get to the graphic screen, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/full_1080.exe'%WORKING_DIRECTORY, '', '', 1)

def startGame(DOCUMENT_ROOT, STEAM_DIRECTORY, GAME_VERSION, loop, reg):
    exeFile = r'{STEAM_DIRECTORY}//{GAME_DIRECTORY}//{GAME_EXECUTOR}'.format(STEAM_DIRECTORY=STEAM_DIRECTORY, GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)

    ## Start game launcher
    # - return 0 and end the whole process, if failed
    # - otherwise, keep running the process
    tries = 10
    while tries != 0:
        startGame = win32api.ShellExecute(1, 'open', exeFile, '', '', 1)
        if startGame:
            break
        if tries == 1 and not startGame:
            saveScreenShoot("OpenLauncherFailed")
            print("****** Failed to open Game Launcer!!! Process stopped ******")
            return 0
        tries -= 1

    time.sleep(10)

    ## Apply ENTER on the launcher to start game
    # return 0, if failed to apply ENTER key on he launcher
    # - otherwise, keep running the process
    tries = 0
    while findWindow(GAME_NAME):
        time.sleep(3)
        key_enter()

        gameHD = findWindow("{GAME_NAME} {GAME_VERSION}".format(GAME_NAME=GAME_NAME, GAME_VERSION=GAME_VERSION))
        if gameHD:
            tries = 0
            break
        elif tries > 10:
            saveScreenShoot("OpenGameFailed")
            print("****** Failed to open Game!!! Process stopped ******")
            return 0
        tries += 1

    ## Give 25 sec for the game to start
    print("Waiting for game to start...")
    time.sleep(35)

    resetMouse()

    time.sleep(5)

    # ****** IN-GAME ACTIONS ******

    # ## Past code ####
    # # 1. Press three "s" keys, and then "ENTER" to option screen
    # # 2. Press three "s" keys, and then "ENTER" to graphic setting
    # startScripts = press_s()
    # time.sleep(1)
    # startScripts = press_s()
    # time.sleep(1)
    # startScripts = press_s()
    # time.sleep(1)
    # startScripts = press_s()
    # time.sleep(1)
    # startScripts = press_enter()
    # time.sleep(3)
    # startScripts = press_s()
    # time.sleep(1)
    # startScripts = press_s()
    # time.sleep(1)
    # startScripts = press_s()
    # time.sleep(1)
    # startScripts = press_enter()
    ####################

    # reactWhole
    if reg == CONFIG_SETTINGS[0]:
        startScripts = reactWhole_2k()
        while(not startScripts):
            startScripts = reactWhole_2k()
    elif reg == CONFIG_SETTINGS[0]:
        startScripts = reactWhole_1080()
        while(not startScripts):
            startScripts = reactWhole_1080()

    # 3. Press "r" key to start benchmarking
    while(loop>0):
        loop -= 1
        time.sleep(10)

        print("Start Benchmarking...")
        startScripts = press_r()
        time.sleep(0.5)
        startScripts = press_r()
        time.sleep(0.5)
        startScripts = press_r()
        time.sleep(0.5)
        startScripts = press_r()


        starting_time = datetime.datetime.now()

        # Waiting for benchmarking
        time.sleep(200)

        # Finding logs
        print("finding logs...")

        # Search for benckmarking logs for 10 times, each times wait for 2 sec
        # if failed, add 1 to {loop} variable for an addition benchmarking
        logs = searchLog(DOCUMENT_ROOT, starting_time)
        tries = 10
        while len(logs) == 0:
            if tries == 0:
                saveScreenShoot("BenchmarkingFailed")
                print("****** Failed benchmarking!!! Retry to bench mark again ******")
                loop += 1
            logs = searchLog(DOCUMENT_ROOT, starting_time)
            tries -= 1
            time.sleep(2)
        if len(logs) != 0:
            print("Succeed benchMarking!! Succeed logs: %s"%logs)
        print("Loop times remained: %s\n"%loop)
    return gameHD

def killProgress(name):
    return os.system('taskkill /F /IM %s'%name)

# STEAM_DIRECTORY = input("Please input your Steam Directory:")
def main(DOCUMENT_ROOT, STEAM_DIRECTORY, loop = 3):

    print("\n")

    GAME_VERSION = "v1.0 build 298.0_64" # This is the latest version at 01/12/2021

    GAME_VERSION = findGameVersion(DOCUMENT_ROOT+GAME_NAME)

    if not GAME_VERSION:
        saveScreenShoot("FineGameVersionFailed")
        print("****** Can't define Game version!!! Process Stopped ******")
        return 0

    for reg in CONFIG_SETTINGS:
        print("Change to Setting file: %s"%reg)
        os.system("REG IMPORT %s"%reg)
        time.sleep(10)
        statusCode = startGame(DOCUMENT_ROOT, STEAM_DIRECTORY, GAME_VERSION, loop, reg)
        if not statusCode:
            saveScreenShoot("OverallError")
            print("****** Something went wrong!!! Process Stopped ******")
            return 0
        statC = killProgress("SOTTR.exe")

    print("###### Finish %s ######\n"%GAME_NAME)
    return 1