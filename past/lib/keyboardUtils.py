import os, sys
import random
import time
import win32api

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.input
import lib.screen
import lib.VK_CODE

WORKING_DIRECTORY = os.getcwd()

# Local variable
STRESS_BM_WAIT_TIME_MIN = 0
STRESS_BM_WAIT_TIME_MAX = 15

ALT_TAB_WAIT_TIME_MIN = 1
ALT_TAB_WAIT_TIME_MAX = 3

KEY_WAIT_TIME_MIN = 0
KEY_WAIT_TIME_MAX = 1

KEY_PRESS_WAIT_TIME_MIN = 0
KEY_PRESS_WAIT_TIME_MAX = 2

RANDOM_WORD_LIST = list(lib.VK_CODE.VK_CODE().getVK_CODE2().keys())

RANDOM_KEY_LIST = [
    "w",
    "a",
    "s",
    "d",
    "e",
    "space",
    "left_click",
    "right_click"
]

MOUSE_LIST = [
    "left_click",
    "right_click",
    "view_upward",
    "view_downward",
    "view_leftward",
    "view_rightward"
]
    # "view_upward",
    # "view_downward",
    # "view_leftward",
    # "view_rightward"

ROTATE_ANGLE = [0, 90, 180, 270]

def normBenchmarking(duration):
    '''
    Perform a normal Benchmarking. No actions would be made.

    @param:
        - duration: duration to perform the normal benchmarking
    '''
    time.sleep(duration)

def stressBenchmarking(duration):
    '''
    Perform a stressed Benchmarking. Randomly performing an ALT+TAB action.

    @param:
        - duration: duration to perform the stressed benchmarking
    '''
    waitTime = 0
    altTabTime = 0
    while(duration >= 0):
        waitTime = random.uniform(STRESS_BM_WAIT_TIME_MIN, STRESS_BM_WAIT_TIME_MAX)
        altTabTime = random.uniform(ALT_TAB_WAIT_TIME_MIN, ALT_TAB_WAIT_TIME_MAX)
        lib.input.key_alt_tab()
        time.sleep(altTabTime)
        lib.input.key_alt_tab()
        time.sleep(waitTime)

        duration -= waitTime
        duration -= altTabTime

def randomCharacterControl(duration):
    '''
    Perform a random Character Control for games.

    @param:
        - duration: duration to perform the random character control
    '''
    waitTime = 0
    altTabTime = 0
    while(duration >= 0):
        waitTime = random.uniform(KEY_WAIT_TIME_MIN, KEY_WAIT_TIME_MAX)
        keyTime = random.uniform(KEY_PRESS_WAIT_TIME_MIN, KEY_PRESS_WAIT_TIME_MAX)
        action = random.choice(RANDOM_KEY_LIST)

        if action in MOUSE_LIST:
            keyTime = mouseCharacterControl(action, keyTime)
        else:
            keyTime = keyCharacterControl(action, keyTime)

        duration -= waitTime
        duration -= keyTime
        time.sleep(waitTime)

def randomTyping(duration):
    '''
    Perform a random Typing Words for Office.

    @param:
        - duration: duration to perform the random typing
    '''
    waitTime = 0
    altTabTime = 0
    while(duration >= 0):
        waitTime = random.uniform(KEY_WAIT_TIME_MIN, KEY_WAIT_TIME_MAX)
        keyTime = random.uniform(KEY_PRESS_WAIT_TIME_MIN, KEY_PRESS_WAIT_TIME_MAX)
        action = random.choice(RANDOM_WORD_LIST)

        keyTime = keyCharacterControl(action, keyTime)

        duration -= waitTime
        duration -= keyTime
        time.sleep(waitTime)

def randomRotate(duration):
    '''
    Perform a random screen rotating

    @param:
        - duration: duration to perform the random screen rotating
    '''
    waitTime = 0
    altTabTime = 0
    while(duration >= 0):
        waitTime = random.uniform(5, STRESS_BM_WAIT_TIME_MAX)

        lib.screen.changeDisplayDirection(0, random.choice(ROTATE_ANGLE))

        duration -= waitTime
        time.sleep(waitTime)

    lib.screen.changeDisplayDirection(0, 0)

def mouseCharacterControl(action, keyTime):
    '''
    A method called by randomCharacterControl() to perform mouse control for characters.

    @param:
        - action: action to perform
        - keyTime: duration to perform the key time
    '''
    res = keyTime
    if action == "view_upward":
        mouse_moveUpWard()
        # lib.input.moveTo(960, 1000, keyTime)
    if action == "view_downward":
        mouse_moveDownWard()
        # lib.input.moveTo(960, 80, keyTime)
    if action == "view_leftward":
        mouse_moveLeftWard()
        # lib.input.moveTo(1800, 540), keyTime
    if action == "view_rightward":
        mouse_moveRightWard()
        # lib.input.moveTo(120, 540, keyTime)
    if action == "left_click":
        lib.input.clickLeft(None, None, keyTime)
    if action == "right_click":
        lib.input.clickRight(None, None, keyTime)
    return res

def keyCharacterControl(action, keyTime):
    '''
    A method called by randomCharacterControl() to perform keyboard control for characters.

    @param:
        - action: action to perform
        - keyTime: duration to perform the key time
    '''
    res = keyTime
    if action == "space":
        lib.input.key_space(keyTime)
    else:
        lib.input.key_input(action, t=keyTime)
    return res

def press_s():
    '''
    Execute s key, by calling the .exe file in "keyassist" folder made by tinytask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/s.exe'%WORKING_DIRECTORY, '', '', 1)

def press_alt_f4():
    '''
    Execute ALT+F4 key, by calling the .exe file in "keyassist" folder made by tinytask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/alt_f4.exe'%WORKING_DIRECTORY, '', '', 1)

def press_enter():
    '''
    Execute enter key, by calling the .exe file in "keyassist" folder made by tinytask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/enter.exe'%WORKING_DIRECTORY, '', '', 1)

def press_r():
    '''
    Execute r key, by calling the .exe file in "keyassist" folder made by tinytask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/r.exe'%WORKING_DIRECTORY, '', '', 1)

def press_w():
    '''
    Execute w key, by calling the .exe file in "keyassist" folder made by tinytask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/w.exe'%WORKING_DIRECTORY, '', '', 1)

def mouse_moveUpWard():
    '''
    Upward move mouse, by calling the .exe file in "keyassist" folder made by tinytask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/mouse_moveUpWard.exe'%WORKING_DIRECTORY, '', '', 1)

def mouse_moveDownWard():
    '''
    Downward move mouse, by calling the .exe file in "keyassist" folder made by tinytask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/mouse_moveDownWard.exe'%WORKING_DIRECTORY, '', '', 1)

def mouse_moveLeftWard():
    '''
    Leftward move mouse, by calling the .exe file in "keyassist" folder made by tinytask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/mouse_moveLeftWard.exe'%WORKING_DIRECTORY, '', '', 1)

def mouse_moveRightWard():
    '''
    Rightward move mouse, by calling the .exe file in "keyassist" folder made by tinytask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/mouse_moveRightWard.exe'%WORKING_DIRECTORY, '', '', 1)

def resetMouse():
    '''
    Reset the mouse position to top-left, by calling the .exe file in "keyassist" folder made by tinytask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/reset_mouse.exe'%WORKING_DIRECTORY, '', '', 1)
