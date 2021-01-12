import datetime
import re, os

def searchFile(pathname, filename):
    '''
    Search for a file
    - return the matched file name
    # 参数1要搜索的路径，参数2要搜索的文件名，可以是正则表代式
    '''
    matchedFile =[]
    for root, dirs, files in os.walk(pathname):
        for file in files:
            if re.match(filename,file):
                fname = os.path.abspath(os.path.join(root,file))
                #print(fname)
                matchedFile.append(fname)
    return matchedFile

def searchLog(DOCUMENT_ROOT, starting_time):
    f = []
    c = starting_time
    while(c < datetime.datetime.now()):
        c = c + datetime.timedelta(minutes=1)
        cur_time = ( c ).strftime("%Y-%m-%d_%H.%M")
        res = searchFile("{DOCUMENT_ROOT}//{GAME_NAME}//".format(DOCUMENT_ROOT=DOCUMENT_ROOT, GAME_NAME=GAME_NAME), "SOTTR_X_%s.*.txt"%(cur_time))
        print(cur_time, " ## ", res)
        if res:
            f.extend(res)
            return f
    return f

GAME_NAME = "Shadow of the Tomb Raider"
DOCUMENT_ROOT = "C:/Users/Navi/Documents//"
loop = 3
starting_time = datetime.datetime(2021, 1, 12, 14, 35, 29, 104646)
logs = searchLog(DOCUMENT_ROOT, starting_time)
tries = 10
while len(logs) == 0:
    if tries == 0:
        print("****** Failed benchmarking!!! Retry to bench mark again ******")
        break
    logs = searchLog(DOCUMENT_ROOT, starting_time)
    tries -= 1
if len(logs) != 0:
    print("Succeed benchMarking!! Succeed logs: %s"%logs)