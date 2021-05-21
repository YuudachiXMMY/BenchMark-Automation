import os, sys, subprocess, psutil
from re import L
import time, datetime
import win32api, win32gui, win32con

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
GAME_DIRECTORY = ""
GAME_EXECUTOR_LIST = [
    "Word",
    "PowerPoint",
    "Excel"
]
GAME_EXECUTOR_LIST = u.searchFile("resources/office", "")
GAME_EXECUTOR = "Word"
GAME_NAME = "Word"

DOCUMENT_ROOT = "" #NOT IN USE
GAME_DIRECTORY = ""
GAME_VERSION = "" #NOT IN USE
LOOP_TIMES = 0
STRESS_TEST = False
PG = ProgramInfo.ProgramInfo(typeDeclear=True)

logger = utils.logger.logger("Office", dir="scripts")

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
    # exeFile = r'{GAME_DIRECTORY}//{GAME_EXECUTOR}'.format(GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)
    exeFile = r"%s"%GAME_EXECUTOR

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

    time.sleep(50)

    ####################################################################################
    # Start Game
    loop = LOOP_TIMES
    while(loop!=0):
        time.sleep(5)

        # Create New
        # tmp = 4
        # while(tmp!=0):
        #     time.sleep(0.5)
        #     tmp = tmp - 1
        #     utils.input.clickLeft(275, 210)

        logger.info(_TAB+'Starting Testing')
        print("Start Testing...")

        ## Perform random Character control for 5 min
        # utils.keyboardUtils.randomTyping(10)
        utils.keyboardUtils.randomRotate(60)

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
    # utils.input.key_alt_f4()
    utils.input.key_alt_f4()
    time.sleep(2)
    # utils.input.key_enter() #Save to default folder

    return startGame

def initialize():
    '''
    '''
    global GAME_DIRECTORY, LOOP_TIMES, STRESS_TEST

    GAME_DIRECTORY = PG.getDirectories().get("Office_Directory") + "//"
    LOOP_TIMES = int(PG.getLoopTimes())
    STRESS_TEST = int(PG.isStressTest())

def start():
    '''
    '''
    global GAME_EXECUTOR, GAME_NAME

    try:
        for tar in GAME_EXECUTOR_LIST:
            GAME_NAME = tar
            GAME_EXECUTOR = tar
            statC = 0
            # Start Game
            try:
                statusCode = startGame()
            except Exception:
                logger.error('Unknown Error: Office.main()', exc_info=True)
            else:
                if statusCode == 0:
                    logger.error('Office: OpenLauncherFailed', exc_info=True)
                    screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OverallError")
                    logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                    print("****** Something went wrong!!! Process Stopped ******\n")
                    return 0
                # try:
                #     logger.info('Killing process: Office.main()')
                #     gameHD = win32gui.FindWindow("{GAME_NAME}".format(GAME_NAME=GAME_NAME))
                #     if gameHD != 0:
                #         statC = u.killProgress("launcher.exe")
                # except Exception:
                #     logger.debug('Killing process: Office.main()')
        logger.info("Finish Office")
        print("###### Finish Office ######")
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