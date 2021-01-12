
import os, signal
import psutil
import ShadowOfTombRaider

def chooseLanguage():
    pass

def showProgramInfo():
    pass

def chooseDocumentDir():

    print("Input the document directory")
    print("Example: C://Users//[USERNAME]//Documents//")

    return input("> ") + "//"

def chooseSteamDir():

    print("Input the Steam directory")
    print("Example: D://SteamLibrary//steamapps//common")

    return input("> ") + "//"

def chooseLoopTimes():

    print("Input the times you want each game to be looped")

    return input("> ")

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

def killProgress(name):
    return os.system('taskkill /F /IM %s'%name)

def main():
    loop = 0

    # chooseLanguage()
    # showProgramInfo()

    DOCUMENT_ROOT =  chooseDocumentDir()
    STEAM_DIRECTORY = chooseSteamDir()

    while loop < 1:
        loop = int(chooseLoopTimes())

    statusCode = ShadowOfTombRaider.main(DOCUMENT_ROOT, STEAM_DIRECTORY, loop)
    statC = killProgress("SOTTR.exe")


    return input("Press ENTER to quit")
    # chooseGame()
    # locateGame()
    # selectScript()

    # chooseGameProfile()

    # startMonitoring()

    # os.system("python main/runScript.py")
    # as_cmd = os.system("python main/monitoringSys.py")

if __name__ == "__main__":
    main()

    # Kill this program itself
    os.kill(os.getpid(), signal.SIGKILL)