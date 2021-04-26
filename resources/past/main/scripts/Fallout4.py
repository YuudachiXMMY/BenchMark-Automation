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
GAME_DIRECTORY = "Fallout 4"
GAME_EXECUTOR = "Fallout4.exe"
GAME_NAME = "Fallout 4"

DOCUMENT_ROOT = "" #NOT IN USE
STEAM_DIRECTORY = ""
LOOP_TIMES = 0
STRESS_TEST = False
PG = ProgramInfo.ProgramInfo(typeDeclear=True)

logger = lib.logger.logger("Fallout4", dir="scripts")

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
    exeFile = r'{STEAM_DIRECTORY}//{GAME_DIRECTORY}//{GAME_EXECUTOR}'.format(STEAM_DIRECTORY=STEAM_DIRECTORY, GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)

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
        if startGame:
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
    while lib.screen.findWindow(GAME_NAME):

        logger.info('Opening Game: %s'%GAME_NAME)
        lib.input.clickLeft(1310, 385)

        time.sleep(10)

        gameHD = lib.screen.findWindow("Fallout4")
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

    ####################################################################################
    # Start Game
    loop = LOOP_TIMES
    while(loop!=0):
        time.sleep(5)

        # Skip Press button to start
        tmp = 10
        while(tmp!=0):
            time.sleep(0.5)
            tmp = tmp - 1
            lib.input.clickLeft(960, 540)

        time.sleep(20)

        lib.keyboardUtils.press_enter()
        time.sleep(10)
        lib.keyboardUtils.press_enter()

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
    global STEAM_DIRECTORY, LOOP_TIMES, STRESS_TEST

    STEAM_DIRECTORY = PG.getSteamDir().get("1") + "//"
    LOOP_TIMES = int(PG.getLoopTimes())
    STRESS_TEST = int(PG.isStressTest())

def start():
    '''
    '''
    statC = 0
    try:
        # Start Game
        try:
            statusCode = startGame()
        except Exception:
            logger.error('Unknown Error: Fallout4.main()', exc_info=True)
        else:
            if statusCode == 0:
                logger.error('Fallout4: OpenLauncherFailed', exc_info=True)
                screenShootName=lib.screen.saveScreenShoot(GAME_NAME, "OverallError")
                logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                print("****** Something went wrong!!! Process Stopped ******\n")
                return 0
            # try:
            #     logger.info('Killing process: Fallout4.main()')
            #     gameHD = win32gui.FindWindow("{GAME_NAME}".format(GAME_NAME=GAME_NAME))
            #     if gameHD != 0:
            #         statC = utils.killProgress("launcher.exe")
            # except Exception:
            #     logger.debug('Killing process: Fallout4.main()')
        logger.info("Finish Fallout4")
        print("###### Finish %s ######"%GAME_NAME)
        return statC
    except Exception:
        logger.error('Unknown Error: Fallout4.main()', exc_info=True)

def main(pg):
    '''
    Main function for Fallout4 automation
    '''
    global PG
    PG = pg

    initialize()
    start()