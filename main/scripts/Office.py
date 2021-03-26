import os, sys, subprocess, psutil
import re
from re import L
import time, datetime
import win32api, win32gui, win32con
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.utils as utils
import lib.logger
import lib.screen
import lib.input
import lib.keyboardUtils
import main.ProgramInfo as ProgramInfo

_TAB = "    "

# Flags
stressTest = True

# Global Variable
WORKING_DIRECTORY = os.getcwd()
GAME_DIRECTORY = "Office"
GAME_EXECUTOR_LIST = [
    "Excel",
    "PowerPoint",
    "Word"
]
GAME_EXECUTOR = "Word"
GAME_NAME = "Word"

DOCUMENT_ROOT = "" #NOT IN USE
GAME_DIRECTORY = ""
GAME_VERSION = "" #NOT IN USE
LOOP_TIMES = 0
STRESS_TEST = False
PG = ProgramInfo.ProgramInfo(typeDeclear=True)

logger = lib.logger.logger("Office", dir="scripts")

# Helper Methods
def resetMouse():
    '''
    Reset the mouse position to top-left, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/reset_mouse.exe'%WORKING_DIRECTORY, '', '', 1)

# Main
def startGame():
    '''
    Scripts to start benchmarking
    '''
    exeFile = r'{GAME_DIRECTORY}//{GAME_EXECUTOR}'.format(GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)

    ## Start game launcher
    # - return 0 and end the whole process, if failed
    # - otherwise, keep running the process
    tries = 10
    while tries != 0:
        logger.info("Opening Game Launcher")
        startGame = win32api.ShellExecute(1, 'open', exeFile, '', '', 1)
        if tries == 1 and not startGame:
            screenShootName=lib.screen.saveScreenShoot(GAME_NAME, "OpenLauncherFailed")
            logger.error('Opening Game Launcher Failed! Screenshoot Created: %s'%screenShootName)
            print("****** Failed to open Game Launcher!!! Process stopped ******\n")
            return 0
        if startGame: ,
            logger.info("Open Game Launcher Succeed")
            print("Open Game Launcher Succeed!!")
            break
        else:
            tries -= 1
            time.sleep(1)

    time.sleep(10)

    ## Apply ENTER on the launcher to start game
    # return 0, if failed to apply ENTER key on he launcher
    # - otherwise, keep running the process
    tries = 0
    while lib.screen.findWindow("Office"):

        logger.info('Opening Game: %s'%GAME_NAME)
        lib.input.clickLeft(1309, 771)

        time.sleep(10)

        gameHD = lib.screen.findWindow("Office")
        if gameHD:
            tries = 0
            break
        elif tries > 10:
            screenShootName=lib.screen.saveScreenShoot(GAME_NAME, "OpenGameFailed")
            logger.error('Opening Game Failed! Screenshoot Created: %s'%screenShootName)
            print("****** Failed to open Game!!! Process stopped ******\n")
            return 0
        tries += 1
        time.sleep(3)

    logger.info(_TAB+'Waiting for game to start')
    ## Give 25 sec for the game to start
    print("Waiting for game to start...")
    time.sleep(60)

    logger.info(_TAB+'Resetting Mouse Position')
    lib.keyboardUtils.resetMouse()

    time.sleep(2)

    ####################################################################################
    # Start Game
    loop = LOOP_TIMES
    while(loop!=0):
        time.sleep(5)

        # Login
        tmp = 10
        while(tmp!=0):
            time.sleep(0.5)
            tmp = tmp - 1
            lib.input.clickLeft(960, 540)

        time.sleep(20)

        logger.info(_TAB+'Starting Testing')
        print("Start Testing...")

        ## Perform random Character control for 5 min
        lib.keyboardUtils.randomCharacterControl(300)

        if loop == -1:
            break
        else:
            loop -= 1
        logger.info('Loop times remained: %s'%loop)
        print("Loop times remained: %s\n"%loop)

    logger.info(_TAB+'All Loop Finishbed')
    print("Finished!")
    ####################################################################################

    # Quit Game
    time.sleep(10)
    # lib.keyboardUtils.press_alt_f4()
    lib.input.key_alt_f4()

    return startGame

def initialize():
    '''
    '''
    global GAME_DIRECTORY, LOOP_TIMES, STRESS_TEST

    GAME_DIRECTORY = PG.getDirectories().get("Office_Directory") + "//"
    LOOP_TIMES = PG.getLoopTimes()
    STRESS_TEST = PG.isStressTest()

def start():
    '''
    '''
    global GAME_EXECUTOR, GAME_NAME

    for tar in GAME_EXECUTOR_LIST:
        GAME_NAME = tar
        GAME_EXECUTOR = tar
        statC = 0
        try:
            # Start Game
            try:
                statusCode = startGame()
            except Exception:
                logger.error('Unknown Error: Office.main()', exc_info=True)
            else:
                if statusCode == 0:
                    logger.error('Office: OpenLauncherFailed', exc_info=True)
                    screenShootName=lib.screen.saveScreenShoot(GAME_NAME, "OverallError")
                    logger.warning(_TAB+'Screenshoot Created: %s'%screenShootName)
                    print("****** Something went wrong!!! Process Stopped ******\n")
                    return 0
                try:
                    logger.info('Killing process: Office.main()')
                    gameHD = win32gui.FindWindow("{GAME_NAME}".format(GAME_NAME=GAME_NAME))
                    if gameHD != 0:
                        statC = utils.killProgress("launcher.exe")
                except Exception:
                    logger.warning('Killing process: Office.main()')
            logger.info("Finish Office")
            print("###### Finish %s ######"%GAME_NAME)
            return statC
        except Exception:
            logger.error('Unknown Error: Office.main()', exc_info=True)

def main(pg):
    '''
    Main function for Office automation
    '''
    global PG
    PG = pg

    initialize()
    start()