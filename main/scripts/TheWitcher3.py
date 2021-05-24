import os, sys, subprocess, psutil
import re
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
GAME_DIRECTORY = "The Witcher 3"
GAME_EXECUTOR = "witcher3.exe"
GAME_NAME = "The Witcher 3"

DOCUMENT_ROOT = "" #NOT IN USE
STEAM_DIRECTORY = ""
LOOP_TIMES = 0
STRESS_TEST = False
PG = ProgramInfo.ProgramInfo(typeDeclear=True)

logger = utils.logger.logger("The Witcher 3", dir="scripts")

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
    # exeFile = r'{STEAM_DIRECTORY}//{GAME_DIRECTORY}//bin//x64//{GAME_EXECUTOR}'.format(STEAM_DIRECTORY=STEAM_DIRECTORY, GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)
    exeFile = '{STEAM_DIRECTORY}//{GAME_DIRECTORY}//bin//x64//'.format(STEAM_DIRECTORY=STEAM_DIRECTORY, GAME_DIRECTORY=GAME_DIRECTORY)

    ## Start game launcher
    # - return 0 and end the whole process, if failed
    # - otherwise, keep running the process
    tries = 10
    logger.info("Opening Game")
    os.chdir(exeFile)
    os.system("start %s"%GAME_EXECUTOR)
    # while tries != 0:
    #     logger.info("Opening Game")
    #     startGame = win32api.ShellExecute(1, 'open', exeFile, '', '', 1)
    #     if tries == 1:
    #         screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OpenFailed")
    #         logger.error('Opening Game Failed! Screenshoot Created: %s'%screenShootName)
    #         print("****** Failed to open Game!!! Process stopped ******\n")
    #         return 0
    #     if startGame:
    #         logger.info("Open Game Succeed")
    #         print("Open Game Succeed!!")
    #         break
    #     else:
    #         tries -= 1
    #         time.sleep(1)

    logger.info(_TAB+'Waiting for game to start')
    ## Give 25 sec for the game to start
    print("Waiting for game to start...")
    time.sleep(30)
    os.chdir(BASE_DIR)

    ####################################################################################
    # Start Game
    loop = LOOP_TIMES
    while(loop!=0):

        time.sleep(20)
        print("s")

        utils.keyboardUtils.callTinyTask("space")
        time.sleep(5)
        utils.keyboardUtils.callTinyTask("e")

        time.sleep(30)

        logger.info(_TAB+'Starting Testing')
        print("Start Testing...")

        ## Perform random Character control for 5 min
        utils.keyboardUtils.randomCharacterControl(300)

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

    utils.keyboardUtils.callTinyTask("esc")
    time.sleep(5)
    utils.keyboardUtils.callTinyTask("up")
    time.sleep(5)
    utils.keyboardUtils.callTinyTask("enter")
    time.sleep(5)
    utils.keyboardUtils.callTinyTask("enter")

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
            logger.error('Unknown Error: The Witcher 3.main()', exc_info=True)
        else:
            if statusCode == 0:
                logger.error('The Witcher 3: OpenLauncherFailed', exc_info=True)
                screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OverallError")
                logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                print("****** Something went wrong!!! Process Stopped ******\n")
                return 0
            # try:
            #     logger.info('Killing process: The Witcher 3.main()')
            #     gameHD = win32gui.FindWindow("{GAME_NAME}".format(GAME_NAME=GAME_NAME))
            #     if gameHD != 0:
            #         statC = u.killProgress("launcher.exe")
            # except Exception:
            #     logger.debug('Killing process: The Witcher 3.main()')
        logger.info("Finish The Witcher 3")
        print("###### Finish %s ######"%GAME_NAME)
        return statC
    except Exception:
        logger.error('Unknown Error: The Witcher 3.main()', exc_info=True)

def main(pg):
    '''
    Main function for The Witcher 3 automation
    '''
    global PG
    PG = pg

    initialize()
    start()