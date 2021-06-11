import os, sys
import time
import win32api, win32con
import pyautogui as pag

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import utils.VK_CODE

## VK_CODE
VK_CODE1 = utils.VK_CODE.VK_CODE().getVK_CODE1()
VK_CODE2 = utils.VK_CODE.VK_CODE().getVK_CODE2()

def key_input(key, t=0.05):
    '''
    Perform a key pressdown and pressup.

    @param:
        - key - a key to be pressed.
        - t - time period in second between pressdown and pressup (default to 0.05).

    @RETURN:
        - 1 - succeed in performing a key pressing process.
        - 0 - failed to perform a key pressing process.
    '''
    if key in VK_CODE2:
        key = VK_CODE2[key]
    if key in VK_CODE1:
        # Pressdown
        win32api.keybd_event(VK_CODE1[key],0,0,0)
        # Duration between pressdown and pressup
        time.sleep(t)
        # Pressup
        win32api.keybd_event(VK_CODE1[key],0,win32con.KEYEVENTF_KEYUP,0)
        return 1
    return 0

def key_inputs(str_input='', t=0.05):
    '''
    Perform a serious of key pressdowns and pressups.

    @param:
        - string of keys - a string of keys to be pressed (default to '').
        - t - time period in second between each key to be pressed (default to 0.05).
    '''
    for k in str_input:
        keyInputStatusCode = key_input(k)
        if keyInputStatusCode == 0:
            pass
        else:
            pass
        time.sleep(t)

def key_enter(t=0.5):
    '''
    Perform a key action of ENTER.

    @param:
        - t - time period in second between pressdown and pressup (default to 0.05).
    '''
    key_input("enter", t)

def key_space(t=0.5):
    '''
    Perform a key action of ENTER.

    @param:
        - t - time period in second between pressdown and pressup (default to 0.05).
    '''
    key_input("spacebar", t)

def key_esc(t=0.5):
    '''
    Perform a key action of ENTER.

    @param:
        - t - time period in second between pressdown and pressup (default to 0.05).
    '''
    key_input("esc", t)

def key_up(t=0.5):
    '''
    Perform a key action of ENTER.

    @param:
        - t - time period in second between pressdown and pressup (default to 0.05).
    '''
    key_input("up_arrow", t)

def key_alt_tab(t=0.5):
    '''
    Perform a key action of ALT + TAB.

    @param:
        - t - time period in second between pressdown and pressup (default to 0.05).
    '''
    win32api.keybd_event(VK_CODE1["alt"],0,0,0)
    win32api.keybd_event(VK_CODE1["tab"],0,0,0)
    time.sleep(t)
    win32api.keybd_event(VK_CODE1["tab"],0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(VK_CODE1["alt"],0,win32con.KEYEVENTF_KEYUP,0)

def key_alt_f4():
    '''
    Perform a key action of ALT + TAB.

    @param:
        - t - time period in second between pressdown and pressup (default to 0.05).
    '''
    win32api.keybd_event(VK_CODE1["alt"],0,0,0)
    time.sleep(0.2)
    win32api.keybd_event(VK_CODE1["F4"],0,0,0)
    time.sleep(0.2)
    win32api.keybd_event(VK_CODE1["F4"],0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.2)
    win32api.keybd_event(VK_CODE1["alt"],0,win32con.KEYEVENTF_KEYUP,0)

def clickLeft(x, y, duration=0):
    '''
    Perform a mouse action of left clicking on screen position at (x, y).

    @param:
        - x - horizontal position to be clicked.
        - y - vertical position to be clicked.
    '''
    if x == None and y == None:
        x, y = win32api.GetCursorPos()
        clickLeft(x, y, duration)
    else:
        # win32api.SetCursorPos((x, y))
        # time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(duration)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def clickRight(x=0, y=0, duration=0):
    '''
    Perform a mouse action of right clicking on screen position at (x, y).

    @param:
        - x - horizontal position to be clicked.
        - y - vertical position to be clicked.
    '''
    if x == None and y == None:
        x, y = win32api.GetCursorPos()
        clickRight(x, y, duration)
    else:
        # win32api.SetCursorPos((x, y))
        # time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        time.sleep(duration)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

def move(start_x, start_y, dest_x, dest_y, duration=0):
    '''
    Perform a mouse action to move the mouse
    from (start_x, start_y) to (dest_x, dest_y) in duration time.

    @param:
        - start_x - horizontal position to start
        - start_y - vertical position to start
        - dest_x - horizontal position to end
        - dest_y - vertical position to end
        - duration - action's duration in seconds
    '''
    win32api.SetCursorPos((start_x, start_y))
    pag.moveTo(dest_x, dest_y, duration=duration, tween=pag.easeInOutQuad)

def moveTo(dest_x, dest_y, duration=0):
    '''
    Perform a mouse action of clicking on screen position at (x, y).

    @param:
        - x - horizontal position to be clicked.
        - y - vertical position to be clicked.
    '''
    start_x, start_y = win32api.GetCursorPos()
    move(start_x, start_y, dest_x, dest_y, duration)

def getMouse(t=0):
    '''
    Get the mouse position and print in the console

    @param:
        - t - period to get the mouse position

    @RETURN:
        - (x, y) - a tuple which x represent the x-position of the mouse and y represent the y-position of the mouse.
    '''
    try:
        while True:
            print("Press Ctrl-C to end")
            screenWidth, screenHeight = pag.size()  # 获取屏幕的尺寸
            x, y = pag.position()  # 返回鼠标的坐标
            print("Screen size: (%s %s),  Position : (%s, %s)\n" % (screenWidth, screenHeight, x, y))  # 打印坐标

            time.sleep(t)  # 每个1s中打印一次 , 并执行清屏
            os.system('cls')  # 执行系统清屏指令
    except KeyboardInterrupt:
        print('end')

def getMouseLogging(t=0):
    '''
    Get the mouse position and print in the console only when the mouse position changes

    @param:
        - t - period to get the mouse position

    @RETURN:
        - (x, y) - a tuple which x represent the x-position of the mouse and y represent the y-position of the mouse.
    '''
    try:
        x, y = pag.position()  # 返回鼠标的坐标
        while True:
            screenWidth, screenHeight = pag.size()  # 获取屏幕的尺寸
            xNew, yNew = pag.position()  # 返回鼠标的坐标
            if xNew != x and yNew != y:
                print("Screen size: (%s %s),  Position : (%s, %s)\n" % (screenWidth, screenHeight, x, y))  # 打印坐标
                x, y = (xNew, yNew)

    except KeyboardInterrupt:
        os.system('cls')  # 执行系统清屏指令
        print('end')