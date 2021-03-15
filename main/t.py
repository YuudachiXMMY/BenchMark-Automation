import os, sys
from os.path import isdir

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from lib import utils


# tmp = input("> ") + "\\"
# data = utils.read_json("data.json")
# data["DIRECTORIES"]['DOCUMENT_RdOOTdd'] = tmp
# utils.write_json("data.json", data)

def chooseDocumentDir():
    '''
    Show a text screen to input the local Document direcotry

    @RETURN
        - a string as input result
    '''
    tmp = input("> ") + "//"
    data = utils.read_json("data.json")
    if data == dict() or not type(data['DIRECTORIES']) is type(dict()):
        data['DIRECTORIES'] = dict()
    data['DIRECTORIES']["DOCUMENT_ROOT"] = tmp
    utils.write_json("data.json", data)

print()
chooseDocumentDir()