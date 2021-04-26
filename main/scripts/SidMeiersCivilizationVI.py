import os, subprocess, psutil
import re
from re import L
import time, datetime
import win32api
import utils.screen

# Global Variable
WORKING_DIRECTORY = os.getcwd()
GAME_DIRECTORY = "Sid Meier's Civilization VI/Base/Binaries/Win64Steam"
GAME_EXECUTOR = "CivilizationVI.exe"
GAME_NAME = "CIVILIZATION VI"
GAME_WINDOW_NAME = "Sid Meier\'s Civilization VI (DX11)"
CONFIG_SETTINGS = ['%s/config_settings/CIVILIZATION_VI/2kTO1080p.exe'%WORKING_DIRECTORY]

# Helper Methodes
def searchLog(DOCUMENT_ROOT, starting_time):
    '''
    Search for Benchmark result under "{DOCUMENT}/{My Games}/Sid Meier's Civilization VI/Logs/"
    - return a LIST of .csv log names, which represents success in benchmarking
    - return [], which represents failure to benchmark
    '''
    f = []
    c = starting_time
    while(c < datetime.datetime.now()):
        cur_time = ( c ).strftime("%Y%m%d-%H%M")
        res = utils.screen.searchFile("{DOCUMENT_ROOT}//My Games//Sid Meier\'s Civilization VI//Logs//".format(DOCUMENT_ROOT=DOCUMENT_ROOT), "Benchmark-%s\d\d.csv"%(cur_time))
        if res:
            f.extend(res)
            return f
        c = c + datetime.timedelta(minutes=1)
    return f

def findGameVersion(DOCUMENT_ROOT):
    '''
    Search for Tomb Raider's version, in the .log file of the game file in\
    system document folder.
    - return 0, if failed to define the game version
    - return game version, if succeed
    '''
    reg = r'v\d+.\d+ build \d+.\d+_\d+'
    tar_f = DOCUMENT_ROOT + "//%s.log"%GAME_NAME
    with open(tar_f) as f:
        for line in f:
            if re.search(reg, line):
                return re.search(reg, line).group()
    return 0

def press_s():
    '''
    Execute s key, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/s.exe'%WORKING_DIRECTORY, '', '', 1)

def press_enter():
    '''
    Execute enter key, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/enter.exe'%WORKING_DIRECTORY, '', '', 1)

def press_r():
    '''
    Execute r key, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/r.exe'%WORKING_DIRECTORY, '', '', 1)

def press_w():
    '''
    Execute w key, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/w.exe'%WORKING_DIRECTORY, '', '', 1)

def resetMouse():
    '''
    Reset the mouse position to top-left, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/reset_mouse.exe'%WORKING_DIRECTORY, '', '', 1)

def launcherStart():
    '''
    Reset the mouse position to top-left, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/CIVILIZATION_VI/CIVILIZATION_VI_launcherStart.exe'%WORKING_DIRECTORY, '', '', 1)

def skipOpening():
    '''
    Reset the mouse position to top-left, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', '%s/keyassist/CIVILIZATION_VI/CIVILIZATION_VI_skipOpening.exe'%WORKING_DIRECTORY, '', '', 1)

def TwoKTO1080p():
    '''
    Reset the mouse position to top-left, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', CONFIG_SETTINGS[0], '', '', 1)

def reactWhole_2k():
    '''
    Apply mouse action to get to the graphic screen, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', "%s/keyassist/CIVILIZATION_VI/CIVILIZATION_VI_2k.exe"%WORKING_DIRECTORY, '', '', 1)

def returnMenu_2k():
    '''
    Apply mouse action to get to the graphic screen, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', "%s/keyassist/CIVILIZATION_VI/returnMenu_2k.exe"%WORKING_DIRECTORY, '', '', 1)

def reactWhole_1080():
    '''
    Apply mouse action to get to the graphic screen, by calling the .exe file in "keyassist" folder made by tinytask
    - return 0, if failed
    - return 1, if succeed
    '''
    return win32api.ShellExecute(1, 'open', "%s/keyassist/CIVILIZATION_VI/CIVILIZATION_VI_2k.exe"%WORKING_DIRECTORY, '', '', 1)

# Bypass Launcher:
# "E:\SteamLibrary\steamapps\common\Sid Meier's Civilization VI\Base\Binaries\Win64Steam\CivilizationVI.exe" %command%
def startGame(DOCUMENT_ROOT, STEAM_DIRECTORY, GAME_VERSION, loop, reg):
    exeFile = r'{STEAM_DIRECTORY}//{GAME_DIRECTORY}//{GAME_EXECUTOR}'.format(STEAM_DIRECTORY=STEAM_DIRECTORY, GAME_DIRECTORY=GAME_DIRECTORY, GAME_EXECUTOR=GAME_EXECUTOR)

    ## Start game launcher
    # - return 0 and end the whole process, if failed
    # - otherwise, keep running the process
    tries = 10
    while tries != 0:
        startGame = win32api.ShellExecute(1, 'open', exeFile, '', '', 1)
        if tries == 1 and not startGame:
            utils.screen.saveScreenShoot(GAME_NAME, "OpenLauncherFailed")
            print("****** Failed to open Game Launcher!!! Process stopped ******")
            return 0
        if startGame:
            print("Open Game Launcher Succeed!!")
            break
        else:
            tries -= 1
            time.sleep(1)

    time.sleep(15)

    ## Apply ENTER on the launcher to start game
    # return 0, if failed to apply ENTER key on he launcher
    # - otherwise, keep running the process
    tries = 0
    while utils.screen.findWindow(GAME_NAME):
        time.sleep(3)

        statC = launcherStart()
        time.sleep(10)

        gameHD = utils.screen.findWindow(GAME_WINDOW_NAME)
        if gameHD:
            tries = 0
            break
        elif tries > 10:
            utils.screen.saveScreenShoot(GAME_NAME, "OpenGameFailed")
            print("****** Failed to open Game!!! Process stopped ******")
            return 0
        tries += 1

    ## Give 25 sec for the game to start
    print("Waiting for game to start...")
    time.sleep(20)
    skipOpening()
    print("Skiping Opening CG...")
    time.sleep(10)
    skipOpening()
    print("Skiping Opening CG again...")
    time.sleep(10)


    resetMouse()

    time.sleep(5)

    # # Change to 1080p at second time
    # if reg == 1:
    #     startScripts = TwoKTO1080p()
    #     time.sleep(20)
    #     while(not startScripts):
    #         startScripts = TwoKTO1080p()
    #         time.sleep(20)

    # 3. Press "r" key to start benchmarking
    while(loop>0):
        loop -= 1


        if reg == 0:
            startScripts = reactWhole_2k()
        # else:
        #     startScripts = reactWhole_1080()

        time.sleep(10)

        print("Start Benchmarking...")

        # 记录开始时间
        starting_time = datetime.datetime.now()

        # Waiting for benchmarking
        time.sleep(160)

        # Finding logs
        print("finding logs...")

        # Search for benchmarking logs for 10 times, each times wait for 2 sec
        # if failed, add 1 to {loop} variable for an addition benchmarking
        logs = searchLog(DOCUMENT_ROOT, starting_time)
        tries = 10
        while len(logs) == 0:
            if tries == 0:
                utils.screen.saveScreenShoot(GAME_NAME, "BenchmarkingFailed")
                print("****** Failed benchmarking!!! Retry to bench mark again ******")
                if reg == 0:
                    startScripts = returnMenu_2k()
                    time.sleep(15)
                loop += 1
                break
            logs = searchLog(DOCUMENT_ROOT, starting_time)
            tries -= 1
            time.sleep(2)
        if len(logs) != 0:
            print("Succeed benchMarking!! Succeed logs: %s"%logs)
            time.sleep(15)
            if reg == 0:
                startScripts = returnMenu_2k()
                time.sleep(15)
        print("Loop times remained: %s\n"%loop)
    return startGame

# STEAM_DIRECTORY = input("Please input your Steam Directory:")
def main(DOCUMENT_ROOT, STEAM_DIRECTORY, loop = 3):

    print("\n")

    GAME_VERSION = "v1.0 build 298.0_64" # This is the latest version at 01/12/2021

    # GAME_VERSION = findGameVersion(DOCUMENT_ROOT+GAME_NAME)

    # if not GAME_VERSION:
    #     utils.screen.saveScreenShoot(GAME_NAME, "FineGameVersionFailed")
    #     print("****** Can't define Game version!!! Process Stopped ******")
    #     return 0
    i = 0
    statusCode = startGame(DOCUMENT_ROOT, STEAM_DIRECTORY, GAME_VERSION, loop, i)
    if not statusCode:
        utils.screen.saveScreenShoot(GAME_NAME, "OverallError")
        print("****** Something went wrong!!! Process Stopped ******")
        return 0
    statC = utils.screen.killProgress("CivilizationVI.exe")

    print("###### Finish %s ######\n"%GAME_NAME)
    return statC