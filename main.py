import json
import os, sys, subprocess, signal
import time
from typing import Tuple
import psutil
import win32gui
import argparse #传参库

# 程序基本库
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import utils.logger
import utils.screen
import utils.sysUtils as utils
import main.ProgramInfo as ProgramInfo