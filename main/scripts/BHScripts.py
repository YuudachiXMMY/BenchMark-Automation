import subprocess, os

WORKING_DIRECTORY = os.getcwd()
script_path = "%s\\BloodHoundScripts\\"%WORKING_DIRECTORY
overallScript = r"\\RunBloodHound.ps1"
scripts = (script_path+r"Scripts\\")
POWERSHELL = r"C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"

Borderlands3 = r"Borderlands3.ps1"
Civilization6 = r"Civilization6.ps1"
CSGO = r"CounterStrikeGo.ps1"
DoomEternal = r"DoomEternal.ps1"
DotA2 = r"DotA2.ps1"
Rainbow6 = r"Rainbow6.ps1"
UnigineHeaven = r"UnigineHeaven.ps1"

bhGameList = [
    Civilization6,
    CSGO,
    DoomEternal,
    DotA2,
    Rainbow6
]

overAllLoop = 1

def runPS(root, sc):
    subprocess.Popen([POWERSHELL, "-File", root+sc])

def runBorderlands3():
    runPS(scripts, Borderlands3)

def runCivilization6():
    runPS(scripts, Civilization6)

def runCSGO():
    runPS(scripts, CSGO)

def runDoomEternal():
    runPS(scripts, DoomEternal)

def runDotA2():
    runPS(scripts, DotA2)

def runRainbow6():
    runPS(scripts, Rainbow6)

def runUnigineHeaven():
    runPS(scripts, UnigineHeaven)

def main(loop=1):
    global overAllLoop

    overAllLoop = loop

    runPS(script_path, overallScript)