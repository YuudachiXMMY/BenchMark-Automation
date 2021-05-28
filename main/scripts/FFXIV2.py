import os, sys
from re import L
import time
import win32api
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
GAME_EXECUTOR = "FFXIVBenchmark.exe"
GAME_NAME = "FINAL FANTASY XIV: 2 Benchmark"

DOCUMENT_ROOT = "" #NOT IN USE
BENCH_DIRECTORY = ""
LOOP_TIMES = 0
STRESS_TEST = False
PG = ProgramInfo.ProgramInfo(typeDeclear=True)

logger = utils.logger.logger("FFXIV2", dir="scripts")

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
    exeFile = r'{BENCH_DIRECTORY}//{GAME_EXECUTOR}'.format(BENCH_DIRECTORY=BENCH_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)

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
    time.sleep(15)

    ####################################################################################
    # Start Game
    loop = LOOP_TIMES
    while(loop!=0):
        time.sleep(5)

        utils.input.key_input("right_arrow")
        time.sleep(3)
        utils.input.key_input("enter")
        time.sleep(3)
        utils.input.key_input("enter")

        time.sleep(30)

        logger.info(_TAB+'Starting Testing')
        print("Start Testing...")

        ## Perform normal Character control for 5 min
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
    utils.input.key_input("esc")
    time.sleep(30)
    # Quit Game Luncher
    utils.keyboardUtils.callTinyTask("alt_f4")
    time.sleep(10)

    return startGame

def initialize():
    '''
    '''
    global BENCH_DIRECTORY, LOOP_TIMES, STRESS_TEST

    BENCH_DIRECTORY = PG.getDirectories().get("FFXIV2_Directory") + "//"
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
            logger.error('Unknown Error: FFXIV2.main()', exc_info=True)
        else:
            if statusCode == 0:
                logger.error('FFXIV2: OpenLauncherFailed', exc_info=True)
                screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OverallError")
                logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                print("****** Something went wrong!!! Process Stopped ******\n")
                return 0
            # try:
            #     logger.info('Killing process: FFXIV2.main()')
            #     gameHD = win32gui.FindWindow("{GAME_NAME}".format(GAME_NAME=GAME_NAME))
            #     if gameHD != 0:
            #         statC = u.killProgress("launcher.exe")
            # except Exception:
            #     logger.debug('Killing process: FFXIV2.main()')
        logger.info("Finish FFXIV2")
        print("###### Finish %s ######"%GAME_NAME)
        return statC
    except Exception:
        logger.error('Unknown Error: FFXIV2.main()', exc_info=True)

def main(pg):
    '''
    Main function for FFXIV2 automation
    '''
    global PG
    PG = pg

    initialize()
    start()