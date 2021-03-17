import json
import os, sys, subprocess, signal
import time
import psutil
import win32gui

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.utils as utils
import lib.logger
import lib.screen
import main.ProgramInfo as ProgramInfo

import main.scripts.ShadowOfTombRaider as ShadowOfTombRaider
import main.scripts.SniperEliteV2 as SniperEliteV2
import main.scripts.BHScripts as BHScripts
import main.scripts.GenshinImpact as GenshinImpact

# HELPER FIELDS
_TAB = "    "
_IN = "> "
_LANGUAGE = 0

# Local Variables
DOCUMENT_ROOT =  ""
STEAM_DIRECTORY = ""
SniperElite_DIRECTORY = ""
AvP_D3D11_DIRECTORY = ""
GenshinImpact_Directory = ""
RUN_LIST = list()

PROGRAM = None

print("Creating Logger")
logger = lib.logger.logger("main")
logger.debug("Created")

# DIY
_READ_LOCAL = True
_CURRENT_RUN_LIST = ["3", "4"] # "1", "2", "5", "6" is excluded for some bugs

overAllLoop = 1
gameLoop = -1
stressTest = True

def initializeProgram():
    '''
    Initialize ProgramInfo Object
    '''
    global PROGRAM

    # Init ProgramInfo object
    PROGRAM = ProgramInfo.ProgramInfo()

def startScripts():
    '''
    '''
    logger.debug("startScripts")
    runList = PROGRAM.getGames()
    logger.debug(runList)
    loop = PROGRAM.getOverAllLoopTimes()
    logger.debug(loop)
    while(loop != 0):
        loop = loop - 1
        if "1" in runList:
            startShadowOfTombRaider()
        if "2" in runList:
            pass
        if "3" in runList:
            logger.debug("SE_V2")
            startSniperEliteV2()
        if "4" in runList:
            startAvP_D3D11()
        if "5" in runList:
            startBHScripts()
            time.sleep(3420)
        if "6" in runList:
            startGenshinImpact()

    # Print Overall loop time remained
    if overAllLoop != 0:
        logger.info("Total Loop time remained: %s"%loop)
        print("Total Loop time remained: %s"%loop)
        print("*"*100 + "\n")

def startShadowOfTombRaider():
    '''
    Start ShadowOfTombRaider Script
    '''
    ## 古墓丽影暗影 2K+1090p Benchmarking
    try:
        logger.info("Starting ShadowOfTombRaider Script")
        statusCode = ShadowOfTombRaider.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing ShadowOfTombRaider.main()', exc_info=True)
    else:
        try:
            gameHD = lib.screen.findWindow("{GAME_DIRECTORY}".format(GAME_DIRECTORY="Shadow of the Tomb Raider"))
            if gameHD != 0:
                try:
                    statC = utils.killProgress("SOTTR.exe")
                except Exception:
                    logger.warning('Killing process Error: ShadowOfTombRaider')
        except Exception:
            logger.warning('Error in Finding ShadowOfTombRaider Game Window', exc_info=True)
        return statusCode

def startSniperEliteV2():
    '''
    Start SniperEliteV2 Script
    '''
    ## 古墓丽影暗影 2K+1090p Benchmarking
    try:
        logger.info("Starting SniperEliteV2 Script")
        statusCode = SniperEliteV2.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing SniperEliteV2.main()', exc_info=True)
    else:
        try:
            gameHD = lib.screen.findWindow("{GAME_DIRECTORY}".format(GAME_DIRECTORY="SniperEliteV2 Benchmark"))
            if gameHD != 0:
                try:
                    statC = utils.killProgress("SniperEliteV2.exe")
                except Exception:
                    logger.warning('Killing process Error: SniperEliteV2')
        except Exception:
            logger.warning('Error in Finding SniperEliteV2 Game Window', exc_info=True)
        return statusCode

def startAvP_D3D11():
    '''
    Start AvP_D3D11 Script
    '''
    ## 古墓丽影暗影 2K+1090p Benchmarking
    try:
        logger.info("Starting AvP_D3D11 Script")
        statusCode = SniperEliteV2.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing AvP_D3D11.main()', exc_info=True)
    else:
        try:
            gameHD = lib.screen.findWindow("{GAME_DIRECTORY}".format(GAME_DIRECTORY="AvP"))
            if gameHD != 0:
                try:
                    statC = utils.killProgress("AvP_D3D11.exe")
                except Exception:
                    logger.warning('Killing process Error: AvP_D3D11')
        except Exception:
            logger.warning('Error in Finding AvP_D3D11 Game Window', exc_info=True)
        return statusCode

def startBHScripts():
    '''
    Start BHScripts Scripts
    '''
    try:
        logger.info("Starting GenshinImpact Script")
        statusCode = BHScripts.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing BHScripts.main()', exc_info=True)
    else:
        return statusCode

def startGenshinImpact():
    '''
    Start GenshinImpact Script
    '''
    ## GenshinImpact
    try:
        logger.info("Starting GenshinImpact Script")
        statusCode = GenshinImpact.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing GenshinImpact.main()', exc_info=True)
    else:
        try:
            gameHD = lib.screen.findWindow("{GAME_DIRECTORY}".format(GAME_DIRECTORY="原神"))
            if gameHD != 0:
                try:
                    statC = utils.killProgress("原神.exe")
                except Exception:
                    logger.warning('Killing process Error: GenshinImpact')
        except Exception:
            logger.warning('Error in Finding GenshinImpact Game Window', exc_info=True)
        return statusCode

def main():
    '''
    Main program of the script
    '''
    print("Main")

    try:
        initializeProgram()
    except Exception:
        print("Error", exc_info=True)

    try:
        startScripts()
    except Exception:
        print("Error", exc_info=True)

    input("Press \'ENTER\' to quit:")

    # # ## 一个监视内存的小工具，暂时不用实装
    # # startMonitoring()

    # # ## Past (not used)
    # # os.system("python main/runScript.py")
    # # as_cmd = os.system("python main/monitoringSys.py")

if __name__ == "__main__":
    main()

    # Kill this program itself
    os.kill(os.getpid(), signal.SIGKILL)