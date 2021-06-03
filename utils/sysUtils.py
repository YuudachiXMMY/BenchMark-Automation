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

def detectCrashDumps(tar="MEMORY.DMP"):
    '''
    Detect whether the window's dump is generated under %LOCALAPPDATA%\CrashDumps

    @param:
        - tar - the target path to copy to (default to "C:\WinDumps")

    @RETURN:
        - True - The dump file is detected
        - False - otherwise, the file is not detected
    '''
    # path = "%LOCALAPPDATA%\CrashDumps"
    src1 = path.expandvars(r'%LOCALAPPDATA%\CrashDumps')
    src2= path.expandvars(r'C:\Windows')
    return searchFile(src1, tar), searchFile(src2, "MEMORY.DMP")

def dealCrashDumps(tar="C:\\WinDumps"):
    '''
    Copy the Windows dump file to the desired location and remove the dump files under %LOCALAPPDATA%\CrashDumps

    @param:
        - tar - the target path to copy to (default to "C:\WinDumps")
    '''

    dst = tar
    files1, files2 = detectCrashDumps()
    while files1 + files2:

        ######################################################
        ## New Code
        src = path.expandvars(r'%LOCALAPPDATA%\CrashDumps')
        for files in os.listdir(src):
            if files == "MEMORY.DMP":
                dst_name = os.path.join(dst, "MEMORY_%s.DMP"%datetime.datetime.now().strftime("%m.%d-%H%M-%Y"))
            else:
                dst_name = os.path.join(dst, files)
            src_name = os.path.join(src, files)
            if os.path.isfile(src_name):
                exe = 'copy ' + src_name +' %s'%dst_name
                os.system(exe)
                if searchFile(src, files):
                    os.system('del '+src_name)
            else:
                print("TAR is not a file!")

        src = "C:\\Windows"
        for files in files2:
            dst_name = os.path.join(dst, "[Windows]MEMORY_%s.DMP"%datetime.datetime.now().strftime("%m.%d-%H%M-%Y"))
            src_name = files
            if os.path.isfile(src_name):
                exe = 'copy ' + src_name +' %s'%dst_name
                os.system(exe)
                if searchFile(src, "MEMORY.DMP"):
                    os.system('del '+src_name)

        # TODO optional: cmd command=> xcopy /s/e "D:\A_FOLDER" "E:\B_FOLDER\"
        files1, files2 = detectCrashDumps()

    ######################################################
    ## Past Code
    # # Copy the dump file
    # tarFile = "MEMORY_" + datetime.datetime.now().strftime("%m.%d-%H%M-%Y")
    # if not tar is None:
    #     exe = 'copy %LOCALAPPDATA%\CrashDumps\MEMORY.DMP '+tar+'\%s.DMP'%tarFile
    #     res = tar+'\%s.DMP'%tarFile
    # else:
    #     exe = 'copy %LOCALAPPDATA%\CrashDumps\MEMORY.DMP %s.DMP'%tarFile
    #     res = '\%s.DMP'%tarFile
    # os.system(exe)
    # if searchFile(tar, tarFile):
    #     os.system('del %LOCALAPPDATA%\CrashDumps\MEMORY.DMP')
    #     return res