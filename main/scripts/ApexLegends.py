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
GAME_DIRECTORY = "Apex Legends"
GAME_EXECUTOR = "r5apex.exe"
GAME_NAME = "Apex Legends"

DOCUMENT_ROOT = "" #NOT IN USE
LOOP_TIMES = 0
STRESS_TEST = False
PG = ProgramInfo.ProgramInfo(typeDeclear=True)

logger = utils.logger.logger("Apex Legends", dir="scripts")

# Main
def startGame():
    '''
    Scripts to start benchmarking
    '''
    exeFile = r'{GAME_DIRECTORY}//{GAME_EXECUTOR}'.format(GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)

    ## Start game
    tries = 10
    while tries != 0:
        logger.info("Opening Game")
        startGame = win32api.ShellExecute(1, 'open', exeFile, '', '', 1)
        if tries == 1 and not startGame:
            screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OpenGameFailed")
            logger.error('Opening Game Failed! Screenshoot Created: %s'%screenShootName)
            print("****** Failed to open Game!!! Process stopped ******\n")
            return 0
        if startGame:
            logger.info("Open Game Succeed")
            print("Open Game Succeed!!")
            break
        else:
            tries -= 1
            time.sleep(1)

    time.sleep(5)

    logger.info(_TAB+'Waiting for game to start')
    ## Give 25 sec for the game to start
    print("Waiting for game to start...")
    time.sleep(80)

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
            utils.input.clickLeft(960, 540)

        time.sleep(30)

        # Change to training mode
        utils.input.clickLeft(195, 805)
        time.sleep(10)
        utils.input.clickLeft(195, 805)

        # Start
        utils.input.clickLeft(220, 945)

        time.sleep(60)

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
    # utils.input.key_alt_f4()
    utils.input.key_alt_f4()

    return startGame

def initialize():
    '''
    '''
    global GAME_DIRECTORY, LOOP_TIMES, STRESS_TEST

    GAME_DIRECTORY = PG.getDirectories().get("ORIGIN_DIRECTORY")["1"] + "//Apex"
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
            logger.error('Unknown Error: ApexLegends.main()', exc_info=True)
        else:
            if statusCode == 0:
                logger.error('Apex Legends: OpenLauncherFailed', exc_info=True)
                screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OverallError")
                logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                print("****** Something went wrong!!! Process Stopped ******\n")
                return 0
            # try:
            #     logger.info('Killing process: ApexLegends.main()')
            #     gameHD = win32gui.FindWindow("{GAME_NAME}".format(GAME_NAME=GAME_NAME))
            #     if gameHD != 0:
            #         statC = u.killProgress("launcher.exe")
            # except Exception:
            #     logger.debug('Killing process: ApexLegends.main()')
        logger.info("Finish Apex Legends")
        print("###### Finish %s ######"%GAME_NAME)
        return statC
    except Exception:
        logger.error('Unknown Error: ApexLegends.main()', exc_info=True)

def main(pg):
    '''
    Main function for Apex Legends automation
    '''
    global PG
    PG = pg

    initialize()
    start()