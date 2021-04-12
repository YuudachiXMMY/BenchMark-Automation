import os, sys, re, subprocess
import json
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import lib.logger

logger = lib.logger.logger("utils", dir='lib')

def searchFile(pathname, filename):
    '''
    Return all matched files under a specific path.

    @param:
        - pathname - a specific path to search for.
        - filename - a filename to search for (Regular Expression can be used).

    @RETURN:
        - A list of sting representing all matched file names
    '''
    logger.info("Searching Files: %s..."%filename)
    matchedFile =[]
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if re.match(filename,file):
                file_name = os.path.abspath(os.path.join(root,file))
                matchedFile.append(file_name)
    logger.info("Matched Files: %s!"%matchedFile)
    return matchedFile

def killProgress(process):
    '''
    A function call a terminal and utilize CMD command to kill a progress.

    @param:
        - process - a process to be forced to kill.

    @RETURN:
        - non-Zero - succeed to call the terminal for killing the process.
        - 0 - failed to open the terminal.
        - -1 - EXCEPTION occurred.
    '''
    logger.info("Killing Process: %s..." % process)
    # return os.system('taskkill /F /IM %s'%name) # An alternative way to kill a process.
    statusCode = 0
    try:
        statusCode = subprocess.Popen('taskkill /F /IM %s'%process, close_fds=True)
    except Exception:
        logger.error("Exception Occurred", exc_info=True)
        return -1
    else:
        logger.info("Process Killed: %s!"%process)
        return statusCode

def read_json(file):
    '''
    Read a .json file and return a json type.

    @param:
        - file - a filename to be read as .json data.

    @RETURN:
        - A Python's Data Object representing the data in the .json file.
        - None - EXCEPTION occurred.
    '''
    try:
        logger.debug("Reading .json: %s..."%file)
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if data == None:
            data = dict()
        logger.debug("Read .json: %s!"%file)
        return data
    except Exception:
        logger.error("Exception Occurred", exc_info=True)
        return None

def write_json(file, data, tar=None):
    '''
    Over-write the .json file with input data.

    @param:
        - file - a filename to be write.
        - data - data to write in the .json file

    @RETURN:
        - 1 - Succeed Over-Write
        - -1 - EXCEPTION occurred.
    '''
    try:
        logger.debug("Writing .json: %s..."%file)

        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f)

        logger.debug("Wrote .json: %s!"%file)
    except Exception:
        logger.error("Exception Occurred", exc_info=True)
        return -1
    return 1

def monitoring():
    '''
    [NOT IN USED]
    A small tool that can detect system RAM
    '''
    # os.system("cmd/k python tests/winMemoryDetect.py")
    subprocess.Popen("cmd/k python tests/winMemoryDetect.py", close_fds=True)

def printAll(data):
    '''
    Print everything in the data Object
    '''
    if type(data) == type(str()):
        print(data)
    else:
        for d in data:
            print(d)