import json
import os, sys, subprocess, signal
import time
from typing import Tuple
import psutil
import win32gui
import argparse #传参库

# 程序基本库
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import utils.logger
import utils.screen
import utils.sysUtils as u
import main.ProgramInfo as ProgramInfo

# Initialize Logger
logger = utils.logger.logger("main")

# 脚本模块
import main.scripts.ShadowOfTombRaider as ShadowOfTombRaider
import main.scripts.AvP_D3D11 as AvP_D3D11
import main.scripts.SniperEliteV2 as SniperEliteV2
import main.scripts.BHScripts as BHScripts
import main.scripts.GenshinImpact as GenshinImpact
import main.scripts.Fallout4 as Fallout4
import main.scripts.Office as Office
import main.scripts.WeHappyFew as WeHappyFew
import main.scripts.ApexLegends as ApexLegends


################################################################################
############################### Global Variables ###############################
################################################################################
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

# Command Line Variables
CMD_readLocal = None

# Global Objects and Variables
PROGRAM = None
overAllLoop = 1
gameLoop = -1
stressTest = True

CRASHDUMP_LOC = u.read_json("config.json")["DIRECTORIES"]["CRASHDUMP_LOC"]

################################################################################
############################### Basic Functions ################################
################################################################################
def CommandLineParser():
    '''
    Parse parameters directly from Command Line and read them as the local variable.
    '''
    global CMD_readLocal, _LANGUAGE
    parser = argparse.ArgumentParser(description='Manual to this script')
    parser.add_argument('--readLocal',
                        type=int,
                        default=0,
                        help="1, to directly run with local settings without user interface; \
                            0, to show a user interface. \
                            (default: show a user interface)")
    parser.add_argument('--language',
                        default="en",
                        help="\"en\" for English Interface; \
                            \"cn\" for Chinese Interface. \
                            (default: \"en\" English)")
    args = parser.parse_args()
    CMD_readLocal = args.readLocal == 1
    _LANGUAGE = args.language

def initializeProgram(language=None, readLocal=None):
    '''
    Initialize ProgramInfo Object
    '''
    global PROGRAM

    # Init ProgramInfo object
    PROGRAM = ProgramInfo.ProgramInfo(language=language, readLocal=readLocal)

def dealWinDumps():
    '''
    Move and log Windows' dump files
    '''
    src1, src2 = u.detectCrashDumps()
    if src1+src2 != []:
        logger.warning("Crash Dump Detected!")
        print("Crash Dump Detected:")
        print(src1+src2)
        dump = u.dealCrashDumps()
        logger.warning("Crash Dump Copied to: %s"%CRASHDUMP_LOC)
        print("Crash Dump Copied to: %s"%CRASHDUMP_LOC)

def startScripts():
    '''
    Get game's run list and loop times and start games' scripts
    '''
    runList = PROGRAM.getGames()
    loop = PROGRAM.getOverAllLoopTimes()
    while(loop != 0):
        loop = loop - 1
        # Shadow of Tomb Raider
        if "1" in runList:
            dealWinDumps()
            startShadowOfTombRaider()
        # Sid Meier's Civilization VI
        if "2" in runList:
            dealWinDumps()
            pass
        # SniperEliteV2 Benchmark
        if "3" in runList:
            dealWinDumps()
            startSniperEliteV2()
        # AlienVSPredictor_D3D11 Benchmark
        if "4" in runList:
            dealWinDumps()
            startAvP_D3D11()
        # BH Scripts
        if "5" in runList:
            dealWinDumps()
            startBHScripts()
            time.sleep(3420)
        # Genshin Impact
        if "6" in runList:
            dealWinDumps()
            startGenshinImpact()
        # Fallout 4
        if "7" in runList:
            dealWinDumps()
            startFallout4()
        # Office
        if "8" in runList:
            dealWinDumps()
            startOffice()
        # We Happy Few
        if "9" in runList:
            dealWinDumps()
            startWeHappyFew()
        # Apex Legends
        if "10" in runList:
            dealWinDumps()
            startApexLegends()

    # Print Overall loop time remained
    if overAllLoop != 0:
        logger.info("Total Loop time remained: %s"%loop)
        print("Total Loop time remained: %s"%loop)
        print("*"*100 + "\n")


################################################################################
############################### Scripts Starters ###############################
################################################################################
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
        return statusCode

def startSniperEliteV2():
    '''
    Start SniperEliteV2 Script
    '''
    ## SniperEliteV2 Benchmarking
    try:
        logger.info("Starting SniperEliteV2 Script")
        statusCode = SniperEliteV2.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing SniperEliteV2.main()', exc_info=True)
    else:
        return statusCode

def startAvP_D3D11():
    '''
    Start AvP_D3D11 Script
    '''
    ## AvP Benchmarking
    try:
        logger.info("Starting AvP_D3D11 Script")
        statusCode = AvP_D3D11.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing AvP_D3D11.main()', exc_info=True)
    else:
        return statusCode

def startBHScripts():
    '''
    Start BHScripts Scripts
    '''
    try:
        logger.info("Starting BHScripts Script")
        statusCode = BHScripts.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing BHScripts.main()', exc_info=True)
    else:
        time.sleep(5400)
        return statusCode

def startGenshinImpact():
    '''
    Start GenshinImpact Script
    '''
    ## GenshinImpact Script
    try:
        logger.info("Starting GenshinImpact Script")
        statusCode = GenshinImpact.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing GenshinImpact.main()', exc_info=True)
    else:
        return statusCode

def startFallout4():
    '''
    Start Fallout4 Script
    '''
    ## Fallout4 Script
    try:
        logger.info("Starting Fallout4 Script")
        statusCode = Fallout4.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing Fallout4.main()', exc_info=True)
    else:
        return statusCode

def startOffice():
    '''
    Start Office Script
    '''
    ## Office Script
    try:
        logger.info("Starting Office Script")
        statusCode = Office.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing Office.main()', exc_info=True)
    else:
        return statusCode

def startWeHappyFew():
    '''
    Start WeHappyFew Script
    '''
    ## WeHappyFew Script
    try:
        logger.info("Starting WeHappyFew Script")
        statusCode = WeHappyFew.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing WeHappyFew.main()', exc_info=True)
    else:
        return statusCode

def startApexLegends():
    '''
    Start ApexLegends Script
    '''
    ## ApexLegends Script
    try:
        logger.info("Starting ApexLegends Script")
        statusCode = ApexLegends.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing ApexLegends.main()', exc_info=True)
    else:
        return statusCode


################################################################################
##################################### Main #####################################
################################################################################
def main():
    '''
    Main program of the script
    '''

    try:
        if CMD_readLocal:
            initializeProgram(language=_LANGUAGE, readLocal=CMD_readLocal)
        else:
            initializeProgram()
    except Exception:
        logger.error("Unknown Error occurred during Initializing")
        print("Unknown Error occurred during Initializing")

    try:
        startScripts()
    except Exception:
        logger.error("Unknown Error occurred during Running Scripts")
        print("Unknown Error occurred during Running Scripts")

    print("*"*50)
    input("Press \'ENTER\' to quit:")

if __name__ == "__main__":
    CommandLineParser()

    try:
        main()
    except KeyboardInterrupt:
        print()
        print("*"*5+' Ctrl+C key input detected. Program Stopped! '+"*"*5)

    # Kill this program itself
    # os.kill(os.getpid(), signal.SIGKILL)