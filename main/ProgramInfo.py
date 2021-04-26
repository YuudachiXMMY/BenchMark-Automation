from logging import setLoggerClass
import os, sys, subprocess
from os.path import isdir, realpath
from typing import List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import utils.sysUtils as u
import utils.logger

_TAB = "    "
_IN = "> "

logger = utils.logger.logger("ProgramInfo", dir='main')

# Available Games
SCRIPT_LIST = {
    "0" : "All",
    "1" : "Shadow of Tomb Raider",
    "2" : "Sid Meier's Civilization VI",
    "3" : "SniperEliteV2 Benchmark",
    "4" : "AlienVSPredictor_D3D11 Benchmark",
    "5" : "Blood Hound Scripts",
    "6" : "Genshin Impact"
}

def isDict(tar):
    '''
    Return True if tar is a dictionary type

    @param:
        - tar - target variable

    @RETURN:
        - true - if tar is a dictionary type
        - false - otherwise
    '''
    return type(tar) == type(dict())

class ProgramInfo():
    '''
    ProgramInfo Class shows this program interact-able screen and save all the user config settings.
    '''

    def __init__(self, language=None, readLocal=None, typeDeclear=False):
        '''
        Construct ProgramInfo

        @param:
            - language - the language of the program: "cn" or "en"
        '''
        if not typeDeclear:
            # Logger
            self.logger = utils.logger.logger("ProgramInfo", dir='main')

            # Language
            if language is None:
                self.chooseLanguage()
            else:
                self._LANGUAGE = language
            self._TEXTS = u.read_json("./resources/tl/programText_%s.json"%self._LANGUAGE)

            self.printOpeningMessage()

            # Choose to Read Local Settings
            # Initialize Local Settings
            if readLocal:
                self.readLocalSettings()
            else:
                self.chooseReadLocalSetting()
                if self._READ_LOCAL:
                    self.readLocalSettings()
                else:
                    self.chooseDocumentDir()
                    self.chooseSteamDir()
                    self.chooseGames()
                    self.chooseLoop()
                    self.chooseStressTest()

            # TODO
            self.setDirectories()

    def printOpeningMessage(self):
        '''
        Print the Opening Message of this program
        '''
        u.printAll(self._TEXTS["opening_message"])

    def initialLogging(self):
        '''
        lib.logger the current overall script settings
        '''
        global logger

        logger.info("Games to Run:")
        for game in self.getGames:
            logger.info(_TAB + "- " + game)
        logger.info("Overall Looped times: %s"%self.getOverAllLoopTimes())
        logger.info("Each Game Looped times: %s"%self.getLoopTimes())
        logger.info("Stress Test Mode: %s"%self.isStressTest)

    def readLocalSettings(self):
        '''
        Read local settings in the settings.json
        '''
        self.writeData(u.read_json("config.json"))

    def chooseLanguage(self):
        '''
        Show a text screen to choose the program displayed language
        '''

        print("Press \"0\" for English")
        print("输入 \"1\" 使用中文 (推荐/RECOMMENDED)")
        t = int(input(_IN).strip())
        # while t != 0 or t != 1:
        #     print("**** Invalid Input! ****")
        #     t = input(_IN)
        if t == 0:
            t = "en"
        elif t == 1:
            t = "cn"
        self._LANGUAGE = t

    def getLanguage(self):
        '''
        Return this program's language

        @RETURN:
            - "cn" - if this program's language is setted to Chinese
            - "en" - if this program's language is setted to English
        '''
        return self._LANGUAGE

    def chooseReadLocalSetting(self):
        '''
        Show a text screen to choose whether to read local setting in settings.json.
        '''
        u.printAll(self._TEXTS["chooseReadLocalSetting"])

        tmp = int(input(_IN).strip())
        self._READ_LOCAL = tmp == 1

    def chooseDocumentDir(self):
        '''
        Show a text screen to input the local Document direcotry
        '''
        u.printAll(self._TEXTS["chooseDocumentDir"])
        res = input(_IN).strip()+ "//"
        self.setDocumentDir(res)

    def setDocumentDir(self, res):
        '''
        Set the ['DIRECTORIES']["DOCUMENT_ROOT"] in data.json
        '''
        data = self.getData()
        if isDict(data) and \
            ( 'DIRECTORIES' not in data or not isDict(data['DIRECTORIES']) ):
            data['DIRECTORIES'] = dict()
        data['DIRECTORIES']["DOCUMENT_ROOT"] = res
        self.writeData(data)

    def getDocumentDir(self):
        '''
        Get the DOCUMENT_ROOT in data.json

        @RETURN:
            - document directory if it is setted
            - None, otherwise
        '''
        data = self.getData()
        if isDict(data) and isDict(data['DIRECTORIES']):
            return data['DIRECTORIES'].get("DOCUMENT_ROOT")
        return None

    def chooseSteamDir(self):
        '''
        A text screen to input the local Steam direcotry
        '''
        u.printAll(self._TEXTS["chooseSteamDir"])
        res =  input(_IN).strip() + "//"
        self.setSteamDir(res)

    def setSteamDir(self, res):
        '''
        Set the ['DIRECTORIES']["STEAM_DIRECTORY"] in data.json
        '''
        data = self.getData()
        if isDict(data) and \
            ( 'DIRECTORIES' not in data or not isDict(data['DIRECTORIES'])):
            data['DIRECTORIES'] = dict()
        if 'STEAM_DIRECTORY' not in data['DIRECTORIES'] or not isDict(data['DIRECTORIES']["STEAM_DIRECTORY"]):
            data['DIRECTORIES']["STEAM_DIRECTORY"] = dict()
        data['DIRECTORIES']["STEAM_DIRECTORY"]["1"] = res
        self.writeData(data)

    def getSteamDir(self):
        '''
        Get the STEAM_DIRECTORY in data.json

        @RETURN:
            - steam directory if it is setted
            - None, otherwise
        '''
        data = self.getData()
        if isDict(data) and isDict(data['DIRECTORIES']):
            return data['DIRECTORIES'].get("STEAM_DIRECTORY")
        return None

    def chooseOverAllLoopTimes(self):
        '''
        A text screen to input overall looped times for the whole script
        '''
        u.printAll(self._TEXTS["chooseOverAllLoopTimes"])
        res = int(input(_IN).strip())
        self.setOverAllLoopTimes(res)

    def setOverAllLoopTimes(self, res):
        '''
        Set the ['RUN']["Overall_loop"] in data.json
        '''
        data = self.getData()
        if isDict(data) and \
            ( 'RUN' not in data or not isDict(data['RUN'])):
            data['RUN'] = dict()
        data['RUN']["Overall_loop"] = res
        self.writeData(data)

    def getOverAllLoopTimes(self):
        '''
        Get the Overall Looped Times in data.json

        @RETURN:
            - overall looped times if it is setted
            - None, otherwise
        '''
        data = self.getData()
        if isDict(data) and 'RUN' in data and isDict(data["RUN"]):
            return data['RUN'].get("Overall_loop")
        return None

    def chooseLoopTimes(self):
        '''
        A text screen to input looped times for each game
        '''
        u.printAll(self._TEXTS["chooseLoopTimes"])
        res = int(input(_IN).strip())
        self.setLoopTimes(res)

    def setLoopTimes(self, res):
        '''
        Set the ['RUN']["Overall_loop"] in data.json
        '''
        data = self.getData()
        if isDict(data) and not isDict(data['RUN']):
            data['RUN'] = dict()
        data['RUN']["Game_loop"] = res
        self.writeData(data)

    def getLoopTimes(self):
        '''
        Get the Each Game's Looped Times in data.json

        @RETURN:
            - each game's looped times if it is setted
            - None, otherwise
        '''
        data = self.getData()
        if isDict(data) and isDict(data['RUN']):
            return data['RUN'].get("Game_loop")
        return None

    def chooseLoop(self):
        '''
        Call the chooseOverAllLoopTimes() and chooseLoopTimes() screen
        '''
        print("\n"+"*"*100)
        self.chooseOverAllLoopTimes()
        self.chooseLoopTimes()
        # overAllLoop = int(self.chooseOverAllLoopTimes())
        # gameLoop = int(self.chooseLoopTimes())

    def getDirectories(self):
        '''
        Get Directories in data.json

        @RETURN:
            - a dictionary of directories
            - None, otherwise
        '''
        data = self.getData()
        if isDict(data):
            return data['DIRECTORIES']
        return None

    def setDirectories(self):
        ''' TODO
        Set config Game Directories
        '''
        pass

    def chooseGames(self):
        '''
        A text screen to select games to be ran. Add selected game to _RUN_LIST.
        '''
        print("\n"+"*"*100)
        tmp = 1
        while(int(tmp) > -1):
            self.printAvailableGames()
            u.printAll(self._TEXTS["chooseGame"])
            u.printAll(self._TEXTS["deleteGameList"])
            u.printAll(self._TEXTS["currentList"])
            print(self.getGames())

            res =  str.lower(input(_IN).strip())
            if res == "r":
                break
            elif res[0] == "d":
                self.deleteGames(res[2])
            elif int(res) >= 0:
                self.setGames(res)
            else:
                continue

            self.setGames(res)

    def getGames(self):
        '''
        Get the current run list ID in data.json

        @RETURN:
            - a list of games if it is setted
            - None, otherwise
        '''
        data = self.getData()
        if isDict(data) and isDict(data['RUN']) and not data['RUN'].get("Run_List") is None:
            return list(data['RUN'].get("Run_List").keys())
        return list()

    def getGamesName(self):
        '''
        Get the current run list Names in data.json

        @RETURN:
            - a list of games if it is setted
            - None, otherwise
        '''
        data = self.getData()
        if isDict(data) and isDict(data['RUN']) and not data['RUN'].get("Run_List") is None:
            return list(data['RUN'].get("Run_List").values())
        return list()

    def setGames(self, res):
        '''
        Set the ['RUN']["Overall_loop"] in data.json
        '''
        data = self.getData()
        if isDict(data) and not isDict(data['RUN']):
            data['RUN'] = dict()
        if res == "0" or \
            "Run_List" not in data['RUN'] or \
            not isDict(data['RUN']["Run_List"]):
            data['RUN']["Run_List"] = dict()
        if res == "0":
            # self.setRunALL()
            for key in SCRIPT_LIST.keys():
                data['RUN']["Run_List"][key] = SCRIPT_LIST[key]
        else:
            if "0" in data['RUN']["Run_List"]:
                del data['RUN']["Run_List"]["0"]
            if res in SCRIPT_LIST:
                data['RUN']["Run_List"][res] = SCRIPT_LIST[res]
        self.writeData(data)

    def deleteGames(self, res):
        '''
        Delete a game in the ['RUN']["Overall_loop"] in data.json
        '''
        data = self.getData()
        if res == "0" or \
            (isDict(data) and not isDict(data['RUN'])):
            data['RUN'] = dict()
        elif res in data['RUN']["Run_List"]:
            del data['RUN']["Run_List"][res]
        self.writeData(data)

    def setRunALL(self):
        '''
        To set the script to run all games
        '''
        data = self.getData()
        if isDict(data) and not isDict(data['RUN']):
            data['RUN'] = dict()
        for key in SCRIPT_LIST.keys():
            data['RUN']["Run_List"][key] = SCRIPT_LIST[key]
        self.writeData(data)

    def chooseStressTest(self):
        '''
        Show a text screen to choose whether to perform Stress Test
        '''
        print("\n"+"*"*100)
        u.printAll(self._TEXTS["chooseStressTest"])
        res = int(input(_IN).strip())

        self.setStressTest(res)

    def setStressTest(self, res):
        '''
        To set the streeTest flag in data.json
        '''
        data = self.getData()
        if isDict(data) and not isDict(data['RUN']):
            data['RUN'] = dict()
        data['RUN']["Stress_Test"] = res
        self.writeData(data)

    def isStressTest(self):
        '''
        Return True if program is performing stress tests

        @RETURN:
            - True - if run in stress test
            - False - otherwise.
        '''
        data = self.getData()
        if isDict(data) and isDict(data['RUN']):
            return data['RUN'].get("Stress_Test") == 1
        return False

    def getText():
        '''
        Return a .json Object for current text.
        '''
        pass

    def getData(self):
        '''
        Return the latest data.json

        @RETURN:
            - a latest Json Object in data.json
        '''
        return u.read_json("data.json")

    def writeData(self, data):
        '''
        Return the latest data.json

        @RETURN:
            - a latest Json Object in data.json
        '''
        u.write_json("data.json", data)

    def printAvailableGames(self):
        '''
        Print current available games for automation
        '''
        u.printAll(self._TEXTS["printAvailableGames"])

    def printCurrentDirectories(self):
        '''
        Print current directories in local settings
        '''
        u.printAll(self._TEXTS["printAvailableGames"][0] + self.getDocumentDir())
        u.printAll(self._TEXTS["printAvailableGames"][1] + self.getSteamDir())
        u.printAll(self._TEXTS["printAvailableGames"][2] + "Not Available")
        u.printAll(self._TEXTS["printAvailableGames"][3] + "Not Available")
        u.printAll(self._TEXTS["printAvailableGames"][4] + "Not Available")
        u.printAll(self._TEXTS["printAvailableGames"][5])
        self.printAvailableGames()

    def chooseGameProfile(self):
        ''' TODO
        A function to manually choose game profiles.
        '''
        GAME_PROFILE = ""
        # os.system("REG IMPORT %s.reg"%GAME_PROFILE)
        subprocess.Popen("REG IMPORT %s.reg"%GAME_PROFILE, close_fds=True)

    def selectScript(self):
        ''' TODO
        A function to select script to run
        '''
        pass