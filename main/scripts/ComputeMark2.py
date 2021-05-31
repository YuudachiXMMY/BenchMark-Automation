import os, sys, subprocess, psutil
import re
from re import L
import time, datetime
import win32api, win32gui, win32con
import uiautomation as auto

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import utils.sysUtils as u
import utils.logger
import utils.screen
import utils.input
import utils.keyboardUtils
import main.ProgramInfo as ProgramInfo

_TAB = "    "

# Flags
stressTest = True

# Global Variable
WORKING_DIRECTORY = os.getcwd()
GAME_EXECUTOR = "ComputeMark.exe"
GAME_NAME = "ComputeMark"

DOCUMENT_ROOT = "" #NOT IN USE
STEAM_DIRECTORY = ""
LOOP_TIMES = 0
STRESS_TEST = False
PG = ProgramInfo.ProgramInfo(typeDeclear=True)

logger = utils.logger.logger("ComputeMark", dir="scripts")

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
    exeFile = r'{STEAM_DIRECTORY}//{GAME_EXECUTOR}'.format(STEAM_DIRECTORY=STEAM_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)

    ## Start game launcher
    # - return 0 and end the whole process, if failed
    # - otherwise, keep running the process
    tries = 10
    while tries != 0:
        logger.info("Opening Game Launcher")
        startGame = win32api.ShellExecute(1, 'open', exeFile, '', '', 1)
        if tries == 1 and not startGame:
            screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OpenLauncherFailed")
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

    logger.info(_TAB+'Waiting for game to start')
    ## Give 25 sec for the game to start
    print("Waiting for game to start...")
    time.sleep(60)

    ####################################################################################
    # Start Game
    loop = LOOP_TIMES
    while(loop!=0):
        time.sleep(5)

        cm = auto.WindowControl(searchDepth=1,Name='ComputeMark')
        cm.SetTopmost(True)

        # Choose Resolution: 1920x1080
        cm.ComboBoxControl(foundIndex=1, Name='').Click()
        cm.ListControl(foundIndex=1, Name='').Click()

        cm.SetTopmost(True)
        # Choose Preset: Extreme
        cm.ComboBoxControl(foundIndex=2, Name='').Click()
        cm.ListControl(foundIndex=1, Name='').Click()

        # Choose Fullscreen
        cm.CheckBoxControl(Name='Fullscreen').Click()

        # Run
        cm.ButtonControl(Name='Run benchmark').Click()

        time.sleep(20)

        utils.input.key_enter()
        time.sleep(10)
        utils.input.key_enter()

        time.sleep(30)

        logger.info(_TAB+'Starting Testing')
        print("Start Testing...")

        ## Perform random Character control for 5 min
        utils.keyboardUtils.normBenchmarking(300)

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
    utils.input.key_esc()
    time.sleep(10)
    utils.input.key_esc()

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
            logger.error('Unknown Error: ComputeMark.main()', exc_info=True)
        else:
            if statusCode == 0:
                logger.error('ComputeMark: OpenLauncherFailed', exc_info=True)
                screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OverallError")
                logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                print("****** Something went wrong!!! Process Stopped ******\n")
                return 0
            # try:
            #     logger.info('Killing process: ComputeMark.main()')
            #     gameHD = win32gui.FindWindow("{GAME_NAME}".format(GAME_NAME=GAME_NAME))
            #     if gameHD != 0:
            #         statC = u.killProgress("launcher.exe")
            # except Exception:
            #     logger.debug('Killing process: ComputeMark.main()')
        logger.info("Finish ComputeMark")
        print("###### Finish %s ######"%GAME_NAME)
        return statC
    except Exception:
        logger.error('Unknown Error: ComputeMark.main()', exc_info=True)

def main(pg):
    '''
    Main function for ComputeMark automation
    '''
    global PG
    PG = pg

    initialize()
    start()