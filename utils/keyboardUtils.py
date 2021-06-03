import os, sys
import random
import time
import win32api

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import utils.input
import utils.screen
import utils.VK_CODE

WORKING_DIRECTORY = os.getcwd()
ROTATE_ANGLE = [0, 90, 180, 270]

# Local variable
# BM stands for BenchMarking
STRESS_BM_WAIT_TIME_MIN = 0
STRESS_BM_WAIT_TIME_MAX = 15

ALT_TAB_WAIT_TIME_MIN = 1
ALT_TAB_WAIT_TIME_MAX = 3

KEY_WAIT_TIME_MIN = 0
KEY_WAIT_TIME_MAX = 1

KEY_PRESS_WAIT_TIME_MIN = 0
KEY_PRESS_WAIT_TIME_MAX = 2

tmp = utils.VK_CODE.VK_CODE().getVK_CODE2().copy()
tmp.update(utils.VK_CODE.VK_CODE().getVK_CODE1())
RANDOM_WORD_LIST = list(tmp.keys())

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
    # "spacebar",

MOUSE_LIST = [
    "left_click",
    "right_click"
]
    # "view_upward",
    # "view_downward",
    # "view_leftward",
    # "view_rightward"

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
        utils.input.key_alt_tab()
        time.sleep(altTabTime)
        utils.input.key_alt_tab()
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
    tmp = RANDOM_KEY_LIST.copy()
    tmp.extend(MOUSE_LIST)
    while(duration >= 0):
        waitTime = random.uniform(KEY_WAIT_TIME_MIN, KEY_WAIT_TIME_MAX)
        keyTime = random.uniform(KEY_PRESS_WAIT_TIME_MIN, KEY_PRESS_WAIT_TIME_MAX)
        action = random.choice(tmp)

        if action in MOUSE_LIST:
            keyTime = mouseCharacterControl(action, keyTime)
        elif action in RANDOM_KEY_LIST:
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
        waitTime = random.uniform(5, 20)

        utils.screen.changeDisplayDirection(0, random.choice(ROTATE_ANGLE))

        duration -= waitTime
        time.sleep(waitTime)

    utils.screen.changeDisplayDirection(0, 0)

def mouseCharacterControl(action, keyTime):
    '''
    A method called by randomCharacterControl() to perform mouse control for characters.

    @param:
        - action: action to perform
        - keyTime: duration to perform the key time
    '''
    res = keyTime
    if action == "view_upward":
        callTinyTask("mouse/moveUpWard")
        # utils.input.moveTo(960, 1000, keyTime)
    if action == "view_downward":
        callTinyTask("mouse/moveDownWard")
        # utils.input.moveTo(960, 80, keyTime)
    if action == "view_leftward":
        callTinyTask("mouse/moveLeftWard")
        # utils.input.moveTo(1800, 540), keyTime
    if action == "view_rightward":
        callTinyTask("mouse/moveRightWard")
        # utils.input.moveTo(120, 540, keyTime)
    if action == "left_click":
        utils.input.clickLeft(None, None, keyTime)
    if action == "right_click":
        utils.input.clickRight(None, None, keyTime)
    return res

def keyCharacterControl(action, keyTime):
    '''
    A method called by randomCharacterControl() to perform keyboard control for characters.

    @param:
        - action: action to perform
        - keyTime: duration to perform the key time
    '''
    # utils.input.key_input(action, keyTime)
    callTinyTask(action)
    time.sleep(keyTime)
    return keyTime

def callTinyTask(TinyTaskFile):
    '''
    Calling the .exe file under "./resources/tinytask/" folder made by TinyTask

    @param:
        - TinyTaskFile: a TinyTask File Name to be performed

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    exe = WORKING_DIRECTORY+'/resources/tinytask/%s.exe'%TinyTaskFile
    return win32api.ShellExecute(1, 'open', exe, '', '', 1)

def tinytask_resetMouse():
    '''
    Reset the mouse position to top-left, by calling "./resources/tinytask/mouse/reset_mouse.exe" file made by TinyTask

    @RETURN:
        - 0 - failed
        - 1 - succeed
    '''
    return callTinyTask("mouse/reset_mouse")