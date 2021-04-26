import os, sys, subprocess, psutil
from re import L
import time, datetime
import win32api, win32gui

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import utils.sysUtils as u
import utils.logger
import utils.screen
import utils.keyboardUtils
import main.ProgramInfo as ProgramInfo

_TAB = "    "

# Flags
STRESS_TEST = True

# Global Variable
WORKING_DIRECTORY = os.getcwd()
GAME_DIRECTORY = "AvP_D3D11_Benchmark"
GAME_EXECUTOR = "AvP_D3D11_Benchmark.exe"
GAME_NAME = "AlienVSPredictor_D3D11 Benchmark"

DOCUMENT_ROOT = ""
BENCH_DIRECTORY = ""
LOOP_TIMES = 0
PG = ProgramInfo.ProgramInfo(typeDeclear=True)

logger = utils.logger.logger("AvP_D3D11", dir="scripts")

# Helper Methodes
def searchLog(starting_time):
    '''
    Search for Benchmark result under "{DOCUMENT}/{AvP_D3D11_Benchmark}"
    - return a LIST of .csv log names, which represents success in benchmarking
    - return [], which represents failure to benchmark
    '''
    f = []
    c = starting_time
    while(c < datetime.datetime.now()):
        cur_time = ( c ).strftime("%Y-%m-%d__%H-%M")
        res = u.searchFile("{DOCUMENT_ROOT}//{GAME_DIRECTORY}//".format(DOCUMENT_ROOT=DOCUMENT_ROOT, GAME_DIRECTORY=GAME_DIRECTORY), "AVP_%s-\d\d.txt"%(cur_time))
        if res:
            f.extend(res)
            return f
        c = c + datetime.timedelta(minutes=1)
    return f

def startGame(loop=-1):
    '''
    Scripts to start benchmarking
    '''
    # Kill Progress if already running
    try:
        gameHD = win32gui.FindWindow(None, "AvP")
        if gameHD != 0:
            statC = u.killProgress("%s"%GAME_EXECUTOR)
    except:
        pass

    exeFile = r'{BENCH_DIRECTORY}//{GAME_EXECUTOR}'.format(BENCH_DIRECTORY=BENCH_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)

    logger.info('Opening Game: %s'%GAME_NAME)
    ## Start game launcher
    # - return 0 and end the whole process, if failed
    # - otherwise, keep running the process
    tries = 10
    while tries != 0:
        startGame = win32api.ShellExecute(1, 'open', exeFile, '', '', 1)
        if tries == 1 and not startGame:
            screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OpenLauncherFailed")
            logger.error(_TAB+'OpenLauncherFailed! Screenshoot Created: %s'%screenShootName)
            print("****** Failed to open Game Launcher!!! Process stopped ******\n")
            return 0
        if startGame:
            logger.info('Open Game Succeed: %s'%GAME_NAME)
            print("Open Game Launcher Succeed!!")
            break
        else:
            tries -= 1
            time.sleep(1)

    logger.info(_TAB+'Waiting for game to start')
    ## Give 4 sec for the game to start
    print("Waiting for game to start...")
    time.sleep(4)

    logger.info(_TAB+'Resetting Mouse Position')
    utils.keyboardUtils.tinytask_resetMouse()

    ####################################################################################
    # Start benchmarking
    loop = LOOP_TIMES
    while(loop!=0):
        time.sleep(5)

        logger.info(_TAB+'Starting Benchmarking')
        print("Start Benchmarking...")

        starting_time = datetime.datetime.now()

        ## Waiting for game to start
        time.sleep(10)
        # Benchmarking
        if STRESS_TEST:
            logger.info(_TAB+'Performing Stress Test')
            utils.keyboardUtils.stressBenchmarking(130)
        else:
            logger.info(_TAB+'Performing Normal Test')
            utils.keyboardUtils.normBenchmarking(130)

        if loop == -1:
            break
        else:
            loop -= 1

            # Finding logs
            logger.info(_TAB+'Searching for Benchmark Log Results')
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
                logger.debug(_TAB+'Benchmarking Succeed with log: %s'%logs)
                print("Succeed benchMarking!! Succeed logs: %s"%logs)
            logger.info('Loop times remained: %s'%loop)
            print("Loop times remained: %s\n"%loop)

    logger.info(_TAB+'All Loop Finishbed')
    print("Finished!")
    ####################################################################################

    return startGame

def initialize():
    '''
    '''
    global DOCUMENT_ROOT, BENCH_DIRECTORY, LOOP_TIMES

    DOCUMENT_ROOT = PG.getDocumentDir() + "//"
    BENCH_DIRECTORY = PG.getDirectories().get("AvP_D3D11_Directory") + "//"
    LOOP_TIMES = int(PG.getLoopTimes())

def start():
    '''
    '''
    statC = 0
    try:
        # Start Game
        try:
            statusCode = startGame()
        except Exception:
            logger.error('Unknown Error: AvP_D3D11.main()', exc_info=True)
        else:
            if statusCode == 0:
                logger.error('AvP_D3D11: OpenLauncherFailed', exc_info=True)
                screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OverallError")
                logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                print("****** Something went wrong!!! Process Stopped ******\n")
                return 0
            # try:
            #     logger.info('Killing process: AvP_D3D11.main()')
            #     gameHD = win32gui.FindWindow("{GAME_NAME}".format(GAME_NAME=GAME_NAME))
            #     if gameHD != 0:
            #         statC = u.killProgress("%s"%GAME_EXECUTOR)
            # except Exception:
            #     logger.debug('Killing process: AvP_D3D11.main()')
        logger.info("Finish AvP_D3D11")
        print("###### Finish %s ######"%GAME_NAME)
        return statC
    except Exception:
        logger.error('Unknown Error: AvP_D3D11.main()', exc_info=True)

# BENCH_DIRECTORY = input("Please input your Steam Directory:")
def main(pg):
    '''
    Main function for AVP automation
    '''
    global PG
    PG = pg

    initialize()
    start()