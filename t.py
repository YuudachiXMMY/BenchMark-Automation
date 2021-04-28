import os, shutil, re
import datetime
from os import path


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

def copyFolder(src, dst):
    '''
    Move all files and folders from src folder to dst folder.
    @param:
        - src - a folder names to be copied.
        - dst - a folder names to copy from src to.
    '''

    if not os.path.isdir(src):
        return
    if not os.path.isdir(dst):
        os.makedirs(dst)

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
                os.system('del '+src+"\%s"%files)
        else:
            print("TAR is not a file!")
    # TODO: cmd command=> xcopy /s/e "D:\A_FOLDER" "E:\B_FOLDER\"
p = path.expandvars(r'%LOCALAPPDATA%\CrashDumps')
dst = "C:\\WinDumps"
copyFolder(p, dst)