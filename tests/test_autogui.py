import time
import pyautogui

def initPos():
    pyautogui.moveTo(0, 0)

initPos()

def getScreenInfo():
    screenWidth, screenHeight = pyautogui.size()
    return screenWidth, screenHeight

def getMouseInfo():
    currentMouseX, currentMouseY = pyautogui.position()
    return currentMouseX, currentMouseY


def test():
    pyautogui.moveTo(100, 150)
    pyautogui.click()
    # 鼠标向下移动10像素
    pyautogui.moveRel(None, 10)
    pyautogui.doubleClick()
    # 用缓动/渐变函数让鼠标2秒后移动到(500,500)位置
    # use tweening/easing function to move mouse over 2 seconds.
    pyautogui.moveTo(1800, 500, duration=2, tween=pyautogui.easeInOutQuad)
    # 在每次输入之间暂停0.25秒
    pyautogui.typewrite('Hello world!', interval=0.25) #输入文本
    pyautogui.press('esc') #按下按键
    pyautogui.keyDown('shift')
    pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
    pyautogui.keyUp('shift')
    pyautogui.hotkey('ctrl', 'c')

def detectMouseInfo():
    prev_mouse = getMouseInfo()

    while True:
        cur_mouse = getMouseInfo()
        if prev_mouse != cur_mouse:
            print( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), getMouseInfo(), "\n" )
            prev_mouse = cur_mouse

detectMouseInfo()