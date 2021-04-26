# coding: UTF-8
import time
from ctypes import *

def enableInputBlock():
    windll.user32.BlockInput(True)
    # user32 = windll.LoadLibrary('user32.dll')
    # user32.BlockInput(True)

def disableInputBlock():
    windll.user32.BlockInput(False) #disable block

def enableInputBlock(duration=5):
    windll.user32.BlockInput(True) #enable block
    time.sleep(duration)
    windll.user32.BlockInput(False) #disable block