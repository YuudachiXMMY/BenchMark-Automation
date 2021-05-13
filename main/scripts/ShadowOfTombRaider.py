import os, sys, subprocess, psutil
import re
from re import L
import time, datetime
import win32api, win32gui
import uiautomation as auto

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import utils.sysUtils as u
import utils.logger
import utils.screen
import utils.keyboardUtils
import main.ProgramInfo as ProgramInfo

_TAB = "    "

# Global Variable
WORKING_DIRECTORY = os.getcwd()
GAME_DIRECTORY = "Shadow of the Tomb Raider"
GAME_EXECUTOR = "SOTTR.exe"
GAME_NAME = "Shadow of the Tomb Raider"
CONFIG_SETTINGS = [
    "resources/config_settings/Shadow_of_the_Tomb_Raider_2k_ultra.reg",
    "resources/config_settings/Shadow_of_the_Tomb_Raider_1080p_ultra.reg"
    ]

STEAM_DIRECTORY = ""
DOCUMENT_ROOT = ""
GAME_VERSION = ""
LOOP_TIMES = 0
PG = ProgramInfo.ProgramInfo(typeDeclear=True)

logger = utils.logger.logger("ShadowOfTombRaider", dir="scripts")

# Helper Methodes
def searchLog(starting_time):
    '''
    Search for Benchmark result under "{DOCUMENT}/Shadow of the Tomb Raider"
    - return a LIST of .txt log names, which represents success in benchmarking
    - return [], which represents failure to benchmark
    '''
    f = []
    c = starting_time
    while(c < datetime.datetime.now()):
        cur_time = ( c ).strftime("%Y-%m-%d_%H.%M")
        res = u.searchFile("{DOCUMENT_ROOT}//{GAME_NAME}//".format(DOCUMENT_ROOT=DOCUMENT_ROOT, GAME_NAME=GAME_NAME), "SOTTR_X_%s.*.txt"%(cur_time))
        if res:
            f.extend(res)
            return f
        c = c + datetime.timedelta(minutes=1)
    return f

def findGameVersion():
    '''
    Search for Tomb Raider's version, in the .log file of the game file in\
    system document folder.
    - return 0, if failed to define the game version
    - return game version, if succeed
    '''
    reg = r'v\d+.\d+ build \d+.\d+_\d+'
    tar_f = DOCUMENT_ROOT+GAME_NAME + "//%s.log"%GAME_NAME
    with open(tar_f) as f:
        for line in f:
            if re.search(reg, line):
                return re.search(reg, line).group()
    return 0

def reactWhole_2k():
    '''
    Apply mouse action to get to the graphic screen, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/ShadowOfTombRaider/ShadowOfTombRaider_full_2k.exe'%WORKING_DIRECTORY, '', '', 1)

def reactWhole_1080():
    '''
    Apply mouse action to get to the graphic screen, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/resources/keyassist/ShadowOfTombRaider/ShadowOfTombRaider_full_1080.exe'%WORKING_DIRECTORY, '', '', 1)

# Main
def startGame(reg):
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

    ## Apply ENTER on the launcher to start game
    # return 0, if failed to apply ENTER key on he launcher
    # - otherwise, keep running the process
    tries = 0
    tmp_gameWindow = "{GAME_NAME} {GAME_VERSION}".format(GAME_NAME=GAME_NAME, GAME_VERSION=GAME_VERSION)
    while utils.screen.findWindow(GAME_NAME):

        logger.info('Opening Game: %s'%GAME_NAME)

        sotr = auto.PaneControl(searchDepth=1,Name=GAME_NAME)
        sotr.SetTopmost(True)
        time.sleep(3)

        utils.keyboardUtils.callTinyTask("enter")
        time.sleep(10)

        gameHD = utils.screen.findWindow(tmp_gameWindow)
        if gameHD:
            tries = 0
            break
        elif tries > 10:
            screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OpenGameFailed")
            logger.error('Opening Game Failed! Screenshoot Created: %s'%screenShootName)
            print("****** Failed to open Game!!! Process stopped ******\n")
            return 0
        tries += 1
        time.sleep(3)

    logger.info(_TAB+'Waiting for game to start')
    ## Give 25 sec for the game to start
    print("Waiting for game to start...")
    time.sleep(35)

    logger.info(_TAB+'Resetting Mouse Position')
    utils.keyboardUtils.tinytask_resetMouse()

    time.sleep(5)

    # reactWhole to start
    if reg == CONFIG_SETTINGS[0]:
        startScripts = reactWhole_2k()
        while(not startScripts):
            startScripts = reactWhole_2k()
    elif reg == CONFIG_SETTINGS[1]:
        startScripts = reactWhole_1080()
        while(not startScripts):
            startScripts = reactWhole_1080()

    ####################################################################################
    # Start Game
    loop = LOOP_TIMES
    while(loop!=0):
        time.sleep(10)

        # 3. Press "r" key to start benchmarking
        print("Start Benchmarking...")
        startScripts = utils.keyboardUtils.callTinyTask("r")
        time.sleep(1)
        startScripts = utils.keyboardUtils.callTinyTask("r")
        time.sleep(1)
        startScripts = utils.keyboardUtils.callTinyTask("r")
        time.sleep(1)
        startScripts = utils.keyboardUtils.callTinyTask("r")
        logger.info(_TAB+'Starting Benchmarking')


        starting_time = datetime.datetime.now()

        # Waiting for benchmarking
        time.sleep(300)
        print(loop)

        if loop == -1:
            print('Finished without Log Searching')
            logger.info(_TAB+'Finished without Log Searching')
            break
        else:
            loop -= 1

            # Finding logs
            logger.info(_TAB+'Searching Logs...')
            print("finding logs...")

            # Search for benchmarking logs for 10 times, each times wait for 2 sec
            # if failed, add 1 to {loop} variable for an addition benchmarking
            logs = searchLog(starting_time)
            tries = 10
            while len(logs) == 0:
                if tries == 0:
                    logger.debug(_TAB+'Benchmark Log Results NOT Found')
                    screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "BenchmarkingFailed")
                    logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                    print("****** Failed benchmarking!!! Retry to bench mark again ******\n")
                    loop += 1
                    break
                logs = searchLog(starting_time)
                tries -= 1
                time.sleep(2)
            if len(logs) != 0:
                print("Succeed benchMarking!! Succeed logs: %s"%logs)
            logger.info('Loop times remained: %s'%loop)
            print("Loop times remained: %s\n"%loop)

    logger.info(_TAB+'All Loop Finishbed')
    print("Finished!")
    ####################################################################################

    # Quit Game
    time.sleep(10)
    utils.keyboardUtils.callTinyTask("alt_f4")
    time.sleep(10)
    utils.keyboardUtils.callTinyTask("enter")

    return startGame

def initialize():
    '''
    '''
    global GAME_VERSION, DOCUMENT_ROOT, STEAM_DIRECTORY, LOOP_TIMES

    DOCUMENT_ROOT = PG.getDocumentDir() + "//"
    STEAM_DIRECTORY = PG.getSteamDir().get("1") + "//"
    LOOP_TIMES = int(PG.getLoopTimes())

    GAME_VERSION = "v1.0 build 298.0_64" # This is the latest version at 01/12/2021
    logger.info("Finding Game Version...")
    GAME_VERSION = findGameVersion() # Temp to find the latest version

    print("\n")

    if not GAME_VERSION:
        screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "FineGameVersionFailed")
        logger.error('Find Game Version Failed! Screenshoot Created: %s'%screenShootName)
        print("****** Can't define Game version!!! Process Stopped ******")
        return 0

    logger.info("Current Game Version: %s"%GAME_VERSION)

def start():
    '''
    '''
    statC = 0
    try:
        # this Loop changes the config files between 1080p & 2k for SOTTR
        for reg in CONFIG_SETTINGS:
            pass
        reg = CONFIG_SETTINGS[1] # only test 1080p
        print("Change to Setting file: %s"%reg)
        # os.system("REG IMPORT %s"%reg)
        subprocess.Popen("REG IMPORT %s"%reg, close_fds=True)
        logger.info('Change to Setting File: %s'%reg)
        time.sleep(10)

        # Start Game
        try:
            statusCode = startGame(reg)
        except Exception:
            logger.error('Unknown Error: ShadowOfTombRaider.main()', exc_info=True)
        else:
            if statusCode == 0:
                logger.error('ShadowOfTombRaider: OpenLauncherFailed', exc_info=True)
                screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OverallError")
                logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                print("****** Something went wrong!!! Process Stopped ******\n")
                return 0
            # try:
            #     logger.info('Killing process: ShadowOfTombRaider.main()')
            #     gameHD = win32gui.FindWindow("{GAME_NAME} {GAME_VERSION}".format(GAME_NAME=GAME_NAME, GAME_VERSION=GAME_VERSION))
            #     if gameHD != 0:
            #         statC = u.killProgress("SOTTR.exe")
            # except Exception:
            #     logger.debug('Killing process: ShadowOfTombRaider.main()')
        logger.info("Finish ShadowOfTombRaider")
        print("###### Finish %s ######"%GAME_NAME)
        return statC
    except Exception:
        logger.error('Unknown Error: ShadowOfTombRaider.main()', exc_info=True)

# STEAM_DIRECTORY = input("Please input your Steam Directory:")
def main(pg):
    '''
    Main function for Shadow of Tomb Raider automation
    '''
    global PG
    PG = pg

    initialize()
    start()