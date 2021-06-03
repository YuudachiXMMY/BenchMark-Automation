
################################################################################
############################### Global Variables ###############################
################################################################################
## Vital Libraries
import os, sys
import time
import argparse #传参库

# Optional Libraries
import json, subprocess, signal
import psutil
import win32gui
from typing import Tuple

# To recognize the path of local libraries
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
## Local Libraries
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
import main.scripts.DMC5 as DMC5
import main.scripts.TheWitcher3 as Witcher3
import main.scripts.ElderScrolls5 as Skyrim
import main.scripts.FFXIV2 as FFXIV2
import main.scripts.FFXIV3 as FFXIV3
import main.scripts.FFXIV4 as FFXIV4
import main.scripts.ComputeMark2 as ComputeMark2
## TODO: Import your New Game's script
# import main.scripts.GameName as GameName


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
RUN_LIST = list()

# Command Line Variables
CMD_readLocal = None

# Global Objects and Variables
PROGRAM = None
overAllLoop = 1
gameLoop = -1

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
    Initialize the global variable PROGRAM by constructing a ProgramInfo Object

    @param:
        - language - Language to be displayed.
        - readLocal - True to read local settings; otherwise, use inputted preference.
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
        print(_TAB+src1+src2)
        dump = u.dealCrashDumps()
        logger.warning("Crash Dump Copied to: %s"%CRASHDUMP_LOC)

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
        # Devil May Cry 5
        if "11" in runList:
            dealWinDumps()
            startDMC5()
        # The Witcher 3
        if "12" in runList:
            dealWinDumps()
            startWitcher3()
        # THe Elder Scrolls 5
        if "13" in runList:
            dealWinDumps()
            startSkyrim()
        # FINAL FANTASY XIV: 2
        if "14" in runList:
            dealWinDumps()
            startFFXIV2()
        # FINAL FANTASY XIV: Heavensward Benchmark
        if "15" in runList:
            dealWinDumps()
            startFFXIV3()
        # FINAL FANTASY XIV: Stormblood Benchmark
        if "16" in runList:
            dealWinDumps()
            startFFXIV4()
        # FINAL FANTASY XIV: Shadow
        if "17" in runList:
            dealWinDumps()
            # startFFXIV4()
        # ComputeMark2
        if "18" in runList:
            dealWinDumps()
            startCM2()

        ## TODO: For new Games
        ## Please replace the "GameName"
        ## "NUMBER" is the number in the values of ["RUN"]["Run_List"] in config.json
        # GameName
        # if "NUMBER" in runList:
        #     dealWinDumps()
        #     startGameName()

    # Print Overall loop time remained
    if overAllLoop != 0:
        logger.info("Total Loop time remained: %s"%loop)
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

def startDMC5():
    '''
    Start Devil May Cry 5
    '''
    try:
        logger.info("Starting Devil May Cry 5 Script")
        statusCode = DMC5.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing DMC5.main()', exc_info=True)
    else:
        return statusCode

def startWitcher3():
    '''
    Start The Witcher 3
    '''
    try:
        logger.info("Starting The Witcher 3 Script")
        statusCode = Witcher3.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing Witcher3.main()', exc_info=True)
    else:
        return statusCode

def startSkyrim():
    '''
    Start The Elder Scrolls 5
    '''
    try:
        logger.info("Starting The Elder Scrolls 5 Script")
        statusCode = Skyrim.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing Skyrim.main()', exc_info=True)
    else:
        return statusCode

def startFFXIV2():
    '''
    Start FINAL FANTASY XIV: 2
    '''
    try:
        logger.info("Starting FINAL FANTASY XIV: 2 Script")
        statusCode = FFXIV2.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing FFXIV2.main()', exc_info=True)
    else:
        return statusCode

def startFFXIV3():
    '''
    Start FINAL FANTASY XIV: Heavensward Benchmark
    '''
    try:
        logger.info("Starting FINAL FANTASY XIV: Heavensward Benchmark Script")
        statusCode = FFXIV3.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing FFXIV3.main()', exc_info=True)
    else:
        return statusCode

def startFFXIV4():
    '''
    Start FINAL FANTASY XIV: Stormblood Benchmark
    '''
    try:
        logger.info("Starting FINAL FANTASY XIV: Stormblood Benchmark Script")
        statusCode = FFXIV4.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing FFXIV4.main()', exc_info=True)
    else:
        return statusCode

def startCM2():
    '''
    Start ComputeMark2
    '''
    try:
        logger.info("Starting ComputeMark2")
        statusCode = ComputeMark2.main(PROGRAM)
    except Exception:
        logger.error('Error in Runing ComputeMark2.main()', exc_info=True)
    else:
        return statusCode

## TODO: For new Games
## Please replace the "GameName"
# def startGameName():
#     '''
#     Start GameName
#     '''
#     try:
#         logger.info("Starting GameName")
#         statusCode = GameName.main(PROGRAM)
#     except Exception:
#         logger.error('Error in Runing GameName.main()', exc_info=True)
#     else:
#         return statusCode


################################################################################
##################################### Main #####################################
################################################################################
def main():
    '''
    Main program of the script
    If any exception occurred, exit with 0; otherwise, exit with 1.
    '''

    try:
        if CMD_readLocal:
            initializeProgram(language=_LANGUAGE, readLocal=CMD_readLocal)
        else:
            initializeProgram()
    except Exception:
        logger.error("Unknown Error occurred during Initializing")
        print("Unknown Error occurred during Initializing")
        print("*"*50)
        input("Press \'ENTER\' to quit:")
        exit(0)

    try:
        startScripts()
    except Exception:
        logger.error("Unknown Error occurred during Running Scripts")
        print("Unknown Error occurred during Running Scripts")
        print("*"*50)
        input("Press \'ENTER\' to quit:")
        exit(0)

    exit(1)

if __name__ == "__main__":
    CommandLineParser()

    try:
        main()
    except KeyboardInterrupt:
        print()
        print("*"*5+' Ctrl+C key input detected. Program Stopped! '+"*"*5)
        exit(1)

    # Kill this program itself
    # os.kill(os.getpid(), signal.SIGKILL)