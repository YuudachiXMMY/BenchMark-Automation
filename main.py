
import os
from multiprocessing import Process
import subprocess
# import main.runScript as rs
# import main.monitoringSys as ms

def chooseLanguage():
    pass

def showProgramInfo():
    pass

def chooseGame():
    pass

def locateGame():
    pass

def chooseGameProfile():
    GAME_PROFILE = ""
    os.system("REG IMPORT %s.reg"%GAME_PROFILE)

def selectScript():
    pass

def startMonitoring():
    os.system("cmd/k python tests/winMemoryDetect.py")

def main():
    chooseLanguage()
    showProgramInfo()

    chooseGame()
    locateGame()
    selectScript()

    chooseGameProfile()

    # startMonitoring()

    # os.system("python main/runScript.py")
    # as_cmd = os.system("python main/monitoringSys.py")



if __name__ == "__main__":
    main()