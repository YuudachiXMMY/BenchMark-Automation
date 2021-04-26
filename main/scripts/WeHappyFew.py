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
GAME_DIRECTORY = "WeHappyFew"
GAME_EXECUTOR = "WeHappyFew.exe"
GAME_NAME = "WeHappyFew"

DOCUMENT_ROOT = "" #NOT IN USE
STEAM_DIRECTORY = ""
LOOP_TIMES = 0
STRESS_TEST = False
PG = ProgramInfo.ProgramInfo(typeDeclear=True)

logger = utils.logger.logger("WeHappyFew", dir="scripts")

# Main
def startGame():
    '''
    Scripts to start benchmarking
    '''
    exeFile = r'{STEAM_DIRECTORY}//{GAME_DIRECTORY}//GlimpseGame//Binaries//Win64//{GAME_EXECUTOR}'.format(STEAM_DIRECTORY=STEAM_DIRECTORY, GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)

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

    time.sleep(10)

    # ## Apply ENTER on the launcher to start game
    # # return 0, if failed to apply ENTER key on he launcher
    # # - otherwise, keep running the process
    # tries = 0
    # while utils.screen.findWindow(GAME_NAME):

    #     logger.info('Opening Game: %s'%GAME_NAME)
    #     utils.input.clickLeft(1310, 385)

    #     time.sleep(10)

    #     gameHD = utils.screen.findWindow("We Happy Few (64-bit, PCD3D_SM5)")
    #     if gameHD:
    #         tries = 0
    #         break
    #     elif tries > 10:
    #         screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OpenGameFailed")
    #         logger.error('Opening Game Failed! Screenshoot Created: %s'%screenShootName)
    #         print("****** Failed to open Game!!! Process stopped ******\n")
    #         return 0
    #     tries += 1
    #     time.sleep(3)

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
            utils.input.clickLeft(960, 540)

        time.sleep(20)

        utils.keyboardUtils.callTinyTask("enter")
        time.sleep(10)
        utils.keyboardUtils.callTinyTask("enter")

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
    # utils.keyboardUtils.press_alt_f4()
    utils.input.key_alt_f4()

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
            logger.error('Unknown Error: WeHappyFew.main()', exc_info=True)
        else:
            if statusCode == 0:
                logger.error('WeHappyFew: OpenLauncherFailed', exc_info=True)
                screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OverallError")
                logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                print("****** Something went wrong!!! Process Stopped ******\n")
                return 0
            # try:
            #     logger.info('Killing process: WeHappyFew.main()')
            #     gameHD = win32gui.FindWindow("{GAME_NAME}".format(GAME_NAME=GAME_NAME))
            #     if gameHD != 0:
            #         statC = u.killProgress("launcher.exe")
            # except Exception:
            #     logger.debug('Killing process: WeHappyFew.main()')
        logger.info("Finish WeHappyFew")
        print("###### Finish %s ######"%GAME_NAME)
        return statC
    except Exception:
        logger.error('Unknown Error: WeHappyFew.main()', exc_info=True)

def main(pg):
    '''
    Main function for WeHappyFew automation
    '''
    global PG
    PG = pg

    initialize()
    start()