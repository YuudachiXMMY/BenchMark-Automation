#####################################################################
############################# Libraries #############################
#####################################################################
## Vital Libraries
import os, sys
from re import L
import time
from uiautomation.uiautomation import DocumentControl
import win32api
import uiautomation as auto

# Optional Libraries
import re, subprocess, psutil, datetime
import win32gui, win32con

# To recognize the path of local libraries
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
## Local Libraries
import utils.sysUtils as u              # Program Utils
import utils.logger                     # Program Logger
import utils.screen                     # Screen Functions
import utils.input                      # Keyboard Actions
import utils.keyboardUtils              # Keyboard Action Utils
import main.ProgramInfo as ProgramInfo  # Vital Program Object


#####################################################################
############################# Variables #############################
#####################################################################
_TAB = "    " # For outputs

# TODO: Global Variable
WORKING_DIRECTORY = os.getcwd() # Program Working Directory
GAME_DIRECTORY = "SSTTEEAAMM"   # Game Folder Name
GAME_EXECUTOR = "SSTTEEAAMM.exe"# Game Executor Name
GAME_NAME = "SSTTEEAAMM"        # Game Window Name

# Variables that Should not be Modified here
DOCUMENT_ROOT = ""      # Document Directory, parsed from ProgramInfo object in initialize() function
BENCH_DIRECTORY = ""    # Independent Directory, parsed from ProgramInfo object in initialize() function
STEAM_DIRECTORY = ""    # Steam Directory, parsed from ProgramInfo object in initialize() function
LOOP_TIMES = 0          # Loop times, parsed from ProgramInfo object in initialize() function
STRESS_TEST = False     # Flag to perform stress test, parsed from ProgramInfo object in initialize() function
PG = ProgramInfo.ProgramInfo(typeDeclear=True) # ProgramInfo object

## Logger
# TODO: Change the name "SSTTEEAAMM"
# Usage:
# [Levels & Code]
#   logger.debug("This is an DEBUG message")
#   logger.info("This is an INFO message")
#   logger.warning("This is an WARNING message")
#   logger.error("This is an ERROR message")
#   logger.critical("This is an CRITICAL message")
# [Console Output]
#   WARNING (default)
# [Log Output]
#   INFO (default)
logger = utils.logger.logger("SSTTEEAAMM", dir="scripts")


#####################################################################
########################## Helper Methods ###########################
#####################################################################
# Helper Methods
def resetMouse():
    '''
    Reset the mouse position to top-left, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed

    (If there's no need to reset mouse position, please feel free to delete this method)
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/reset_mouse.exe'%WORKING_DIRECTORY, '', '', 1)


#####################################################################
############################ Main Script ############################
#####################################################################
# Main
def startGame():
    '''
    Scripts to start benchmarking
    '''

    ## TODO: A variable of the full path for a Game's Executor/Luncher
    # Example 1: Steam Dependent Games
    #   Fullpath: F:\SteamLibrary\steamapps\common\Skyrim\SkyrimLauncher.exe
    #   exeFile = r'{STEAM_DIRECTORY}//{GAME_DIRECTORY}//{GAME_EXECUTOR}'.format(STEAM_DIRECTORY=STEAM_DIRECTORY, GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)
    #   where: STEAM_DIRECTORY = "F:\SteamLibrary\steamapps\common\"
    #          GAME_DIRECTORY = "Skyrim"
    #          GAME_EXECUTOR = "SkyrimLauncher.exe"
    # Example 2: Independent Games
    #   Fullpath: C://Program Files (x86)//Rebellion//AvP D3D11 Benchmark//AvP_D3D11_Benchmark.exe
    #   exeFile = r'{BENCH_DIRECTORY}//{GAME_DIRECTORY}//{GAME_EXECUTOR}'.format(BENCH_DIRECTORY=BENCH_DIRECTORY, GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)
    #   where: BENCH_DIRECTORY = "C://Program Files (x86)//Rebellion//"
    #          GAME_DIRECTORY = "AvP D3D11 Benchmark"
    #          GAME_EXECUTOR = "AvP_D3D11_Benchmark.exe"
    # NOTE: the three variables above should be parsed in the initialize()
    #       function below
    exeFile = r'{STEAM_DIRECTORY}//{GAME_DIRECTORY}//{GAME_EXECUTOR}'.format(STEAM_DIRECTORY=STEAM_DIRECTORY, GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)

    #################################################################
    ###################### Start Game Launcher ######################
    #################################################################
    ## TODO: Start a Game Launcher
    # Try 10 times with period of 1 second to open the launcher
    # - return 0 and end the whole process, if failed
    # - otherwise, keep running the process
    # (If a game does not have any launchers, please delete these codes)
    tries = 10
    while tries != 0:
        logger.info("Opening Game Launcher")
        startGame = win32api.ShellExecute(1, 'open', exeFile, '', '', 1)

        if tries == 1 and not startGame:
            ## Failed to open the Game Launcher after 10 times
            # Make a screenshot and log error message, then return 0 to the main program.
            screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OpenLauncherFailed")
            logger.error('Opening Game Launcher Failed! Screenshoot Created: %s'%screenShootName)
            print("****** Failed to open Game Launcher!!! Process stopped ******\n")
            return 0
        if startGame:
            ## Succeed to open the Game Launcher
            # Log and print message to both Log and Console
            logger.info("Open Game Launcher Succeed")
            print("Open Game Launcher Succeed!!")
            break
        else:
            ## Failed to open the Game Launcher, and keep trying after 1 second
            tries -= 1
            time.sleep(1) # Waiting for 1 second

    time.sleep(10) # Waiting for 10 second to start the launcher


    #################################################################
    ########################## Start Game ###########################
    #################################################################
    ## TODO: If any action (e.g. Key/Mouse inputs like "enter") should be taken
    #        on the Launcher to start the Game, Please apply these actions here:
    # Example:
    #   Apply ENTER on the launcher to start game
    #   - return 0, if failed to apply ENTER key on he launcher
    #   - otherwise, keep running the process
    tries = 0
    # TODO: GAME_NAME should be the window name of the Game, not Game Executor!
    # so please update GAME_NAME variable at the very top of this script
    while utils.screen.findWindow(GAME_NAME):

        logger.info('Opening Game: %s'%GAME_NAME)

        #################################################################
        ## TODO: To Start the Game on Game Launcher
        # Please ONLY choose ONE of the following methods, which can best
        # apply to the Game, and delete codes for other methods


        ## [Method 1] Click at a specific position on the Game Launcher
        utils.input.clickLeft(1310, 385)


        ## [Method 2] Directly press ENTER on the Game Launcher
        utils.input.key_enter()


        ## [Method 3] Call a combination of actions recorded by TinyTask
        # The combination of actions should be an ".exe" file
        # under the folder ".\resources\tinytask\"
        utils.keyboardUtils.callTinyTask("")


        ## [Method 4] Detect the buttons Position by using UIAutomation
        ## Can be viewed by "Accessibility Insights" tool, by Microsoft.
        # Detect the Launcher window
        #!! Be care of the Control type
        #!! Here, the control type is "PaneControl", sometimes it can be "WindowControl" or other
        app = auto.PaneControl(searchDepth=1,Name='SSTTEEAAMM')

        # Set the launcher window to the very top of the screen
        app.SetTopmost(True)

        # Find the Start Button
        # foundIndex=INT - the index of the Start Button
        # Name=STRING - the name of the Start Button (in most cases, STRING is empty, which is "")
        #!! Be care of the Control type
        #!! In most cases, it is "ButtonControl", sometimes it can be "ImageControl" or other
        app.ButtonControl(foundIndex=16, Name='').Click()

        #################################################################

        time.sleep(10) # Waiting for 10 seconds

        gameHD = utils.screen.findWindow(GAME_NAME)
        if gameHD:
            ## Succeed to find the Game Window, keep running the program
            tries = 0
            break
        elif tries > 10:
            ## Failed to find the Game Window after 10 times
            # Make a screenshot and log error message, then return 0 to the main program.
            screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OpenGameFailed")
            logger.error('Opening Game Failed! Screenshoot Created: %s'%screenShootName)
            print("****** Failed to open Game!!! Process stopped ******\n")
            return 0
        tries += 1


    ## Give 60 seconds for the Game to start
    logger.info(_TAB+'Waiting for game to start')
    print("Waiting for game to start...")
    time.sleep(60)


    #################################################################
    ######################### Start Gaming ##########################
    #################################################################
    loop = LOOP_TIMES
    while(loop!=0):
        time.sleep(5)

        ## TODO: Skip animations by Pressing Left Mouse button 10 times
        # with a period of 0.5 seconds
        # (This code can be deleted and replaced by pure waiting,
        # using time.sleep(60))
        tmp = 10
        while(tmp!=0):
            time.sleep(0.5)
            tmp = tmp - 1
            utils.input.clickLeft(960, 540)

        ## TODO: Actions need to be taken to start gaming
        # Can use alternative methods, just like we've did above for Game Launcher
        utils.input.key_enter() # Directly press enter


        time.sleep(30) # Wait for 30 seconds loading

        logger.info(_TAB+'Starting Testing')
        print("Start Testing...")

        ## TODO: Perform Benchmark Options for 5 min
        # Please Choose only one of the following
        utils.keyboardUtils.normBenchmarking(300)       # Without any actions
        # utils.keyboardUtils.randomCharacterControl(300) # Randomly Control the Character
        # utils.keyboardUtils.stressBenchmarking(300)     # Randomly performing ALT+TAB action

        if loop == -1:
            break

        else:
            loop -= 1
        logger.info('Loop times remained: %s'%loop)
        print("Loop times remained: %s\n"%loop)

    logger.info(_TAB+'All Loop Finishbed')
    print("Finished!")
    ####################################################################################

    ## TODO: Actions need to be taken to Quit Game
    # Can use alternative methods, just like we've did above for Game Launcher
    utils.input.key_alt_f4()
    utils.input.key_enter()
    # utils.keyboardUtils.callTinyTask("alt_f4")

    return startGame

def initialize():
    '''
    Parse Directory from the ProgramInfo object, and kindly use the build-in
    functions to find the desired key-value pairs in config.json.
    '''
    ## TODO: Change codes to parsed directories that are needed

    ## If document directory is needed, please un-comment the following codes,
    ##  otherwise, feel free to delete it.
    # global DOCUMENT_ROOT
    # DOCUMENT_ROOT = PG.getDocumentDir() + "//"

    ## If a game is under steam directory, please use the following
    global STEAM_DIRECTORY
    STEAM_DIRECTORY = PG.getSteamDir().get("1") + "//"  # Parse the Steam Directory

    ## If a game is under an independent directory, please add its diretory in the config.json
    #  and use this code
    global BENCH_DIRECTORY
    BENCH_DIRECTORY = PG.getDirectories().get("AvP_D3D11_Directory") + "//"

    ## Stuffs that should not be modified
    global LOOP_TIMES, STRESS_TEST
    LOOP_TIMES = int(PG.getLoopTimes())                 # Parse the Loop times
    STRESS_TEST = int(PG.isStressTest())                # Parse the Stress Test Flag

def start():
    '''
    (Please ONLY modify the SSTTEEAAMM parts for this function)
    '''
    statC = 0
    try:
        # Start Game
        try:
            statusCode = startGame()
        except Exception:
            logger.error('Unknown Error: SSTTEEAAMM.main()', exc_info=True)
        else:
            if statusCode == 0:
                logger.error('SSTTEEAAMM: OpenLauncherFailed', exc_info=True)
                screenShootName=utils.screen.saveScreenShoot(GAME_NAME, "OverallError")
                logger.debug(_TAB+'Screenshoot Created: %s'%screenShootName)
                print("****** Something went wrong!!! Process Stopped ******\n")
                return 0
        logger.info("Finish SSTTEEAAMM")
        print("###### Finish %s ######"%GAME_NAME)
        return statC
    except Exception:
        logger.error('Unknown Error: SSTTEEAAMM.main()', exc_info=True)

def main(pg):
    '''
    Main function for SSTTEEAAMM automation
    '''
    global PG
    PG = pg

    initialize()
    start()