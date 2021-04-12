import os, sys, re, subprocess
import time
import random
import win32gui, win32api, win32con
from PIL import ImageGrab

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.logger

# Current Screen Size: [horizontal_length, vertical_length]
SCREEN_SIZE = (win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN))
logger = lib.logger.logger("screen", dir='lib')

def makeScreenShoot():
    '''
    Make a screenshoot of the current Windows screen.

    @RETURN:
        - A ImageGrab Object representing the current Windows screenshoot.
        - None - EXCEPTION occurred.
    '''
    try:
        logger.debug("Screenshoot made.")
        return ImageGrab.grab(bbox=(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1]))
    except Exception:
        logger.error("Exception Occurred", exc_info=True)
        return None

def saveScreenShoot(task, error=''):
    '''
    Save a screenshoot under "./errors." folder.

    @param:
        - task - the current task that is running.
        - error - error message (default to '').

    @RETURN:
        - A string representing the screenshoot file name.
        - None - EXCEPTION occurred.
    '''
    try:
        img = makeScreenShoot()
        screenShootName = '{task}_{time}.jpg'.format(task=task, time=time.strftime("%m_%d_%H_%M_%S", time.localtime()))
        if error != '':
            screenShootName = '[%s] '%error + screenShootName
        img.save("errors/%s"%screenShootName)
        logger.info("Saved Screen Shoot: %s"%screenShootName)
        return screenShootName
    except Exception:
        logger.error("Exception Occurred", exc_info=True)
        return None

def findWindow(windowName):
    '''
    Find a displayed window in 15 second with 5 tries.

    @param:
        - windowName - a windows to be found displayed.

    @RETURN:
        - non-Zero - representing the window's HD.
        - 0 - failed to find the window and will save a screenshoot.
        - None - EXCEPTION occurred.
    '''
    try:
        logger.info("Finding Window: %s..." % windowName)
        winHD = win32gui.FindWindow(None, windowName)
        tries = 0
        while winHD == 0:
            time.sleep(3)
            winHD = win32gui.FindWindow(None, windowName)
            if tries > 5:
                saveScreenShoot(windowName, "FindWindowFailed")
                logger.warning("Failed to Find Window: %s"%windowName)
                return 0
            tries += 1
        return winHD
    except Exception:
        logger.error("Exception Occurred", exc_info=True)
        return None

def changeDisplayDirection(deviceIndex, angle):
    '''
    Rotate the Display Screen's Direction

    @param:
        - deviceIndex - display device index
        - angle - angle to be rotated

    @RETURN:
        - True - succeed in rotating the screen.
        - False - failed to rotate the screen.
    '''
    # if not hasDisplayDevice(deviceIndex):
    #     return
    try:
        device = win32api.EnumDisplayDevices(None, deviceIndex)
        dm = win32api.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
        if angle == 90:
            dm.DisplayOrientation = win32con.DMDO_90 #待改变的值
            #以下的720或者1280 代表我的屏幕的长宽
            #在应用项目的时候,建议使用GetSystemMetrics 动态获取长宽
            #在每次改变方向的时候,都要判断是否需要交换屏幕的长宽
            if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != 720:
                dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth

        elif angle == 180:
            dm.DisplayOrientation = win32con.DMDO_180
            if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != 1280:
                dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth

        elif angle == 270:
            dm.DisplayOrientation = win32con.DMDO_270
            if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != 720:
                dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth

        elif angle == 0:
            dm.DisplayOrientation = win32con.DMDO_DEFAULT
            if win32api.GetSystemMetrics(win32con.SM_CXSCREEN) != 1280:
                dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth

        win32api.ChangeDisplaySettingsEx(device.DeviceName,dm)

        return True

    except Exception:
        return False

def hasDisplayDevice(deviceIndex):
    '''
    Check whether the screen device represented by the index is connected

    @param:
        - deviceIndex - the index representing a screen monitor

    @RETURN:
        - True - the index is valid the screen monitor exist
        - False
    '''
    if type(deviceIndex) != int:
        return False
    try:
        device = win32api.EnumDisplayDevices(None, 1)
        dm = win32api.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
        return True
    except Exception:
        return False