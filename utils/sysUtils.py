import os, re, subprocess
from os import path
import datetime
import json

def searchFile(pathname, filename):
    '''
    Return all matched files under a specific path.

    @param:
        - pathname - a specific path to search for.
        - filename - a filename to search for (Regular Expression can be used).

    @RETURN:
        - A list of sting representing all matched file names
    '''
    matchedFile =[]
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if re.match(filename,file):
                file_name = os.path.abspath(os.path.join(root,file))
                matchedFile.append(file_name)
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
    # return os.system('taskkill /F /IM %s'%name) # An alternative way to kill a process.
    statusCode = 0
    try:
        statusCode = subprocess.Popen('taskkill /F /IM %s'%process, close_fds=True)
    except Exception:
        return -1
    else:
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
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if data == None:
            data = dict()
        return data
    except Exception:
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
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
    except Exception:
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

def detectCrashDumps():
    '''
    Detect whether the window's dump is generated under %LOCALAPPDATA%\CrashDumps

    @RETURN:
        - True - The dump file is detected
        - False - otherwise, the file is not detected
    '''
    # path = "%LOCALAPPDATA%\CrashDumps"
    p = path.expandvars(r'%LOCALAPPDATA%\CrashDumps')
    tar = "MEMORY.DMP"
    return searchFile(p, tar)

def dealCrashDumps(p="C:\\WinDumps"):
    '''
    Copy the Windows dump file to the desired location and remove the dump files under %LOCALAPPDATA%\CrashDumps

    @param:
        - p - the target path to copy to (default to "C:\WinDumps")

    @RETURN:
        - a copied file name with full path
    '''
    while detectCrashDumps():
        # Copy the dump file
        tarFile = "MEMORY_" + datetime.datetime.now().strftime("%m.%d-%H%M-%Y")
        if not p is None:
            exe = 'copy %LOCALAPPDATA%\CrashDumps\MEMORY.DMP '+p+'\%s.DMP'%tarFile
            res = p+'\%s.DMP'%tarFile
        else:
            exe = 'copy %LOCALAPPDATA%\CrashDumps\MEMORY.DMP %s.DMP'%tarFile
            res = '\%s.DMP'%tarFile
        os.system(exe)
        if searchFile(p, tarFile):
            os.system('del %LOCALAPPDATA%\CrashDumps\MEMORY.DMP')
            return res