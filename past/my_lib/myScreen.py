import time
import re, sys
import win32gui
import win32api
import win32con
from PIL import ImageGrab

class myScreen():

    def __init__(self, task=''):
        self.width, self.height = pyautogui.size()
        self.task = task
        self._handle = '.*Google*.'

    def getScreenWidth(self):
        return self.width

    def getScreenHeight(self):
        return self.height

    def getScreenInfo(self):
        return self.getScreenWidth(), self.getScreenHeight()

    def makeScreenShoot(self):
        return ImageGrab.grab(bbox=(0, 0, self.getScreenWidth(), self.getScreenHeight()))

    def saveScreenShoot(self):
        img = self.makeScreenShoot()
        img.save('{task}_{time}.jpg'.format(task=self.task, time=time.strftime("%m_%d_%H_%M_%S", time.localtime())))

    def getMousePosition(self):
        cur_mouseXpos, cur_mouseYpos = pyautogui.position()
        return cur_mouseXpos, cur_mouseYpos

    def detectMouseMovement(self):
        prev_mouse = self.getMousePosition()

        while True:
            cur_mouse = self.getMousePosition()
            if prev_mouse != cur_mouse:
                print( time.strftime("%H:%M:%S", time.localtime()), cur_mouse, "\n" )
                prev_mouse = cur_mouse

    # def find_window(self, window_name, class_name = None):
    #     '''find a window by its window_name'''
    #     self._handle = win32gui.FindWindow(class_name, window_name)

    # def __window_enum_callback(self, hwnd, wildcard):
    #     '''pass to win32gui.EnumWindows() to check all the opened windows'''
    #     if re.match(wildcard, str(win32gui.GetWindowsText(hwnd))) != None:
    #         self._handle = hwnd

    # def find_window_wildcard(self, wildcard):
    #     self._handle = None
    #     win32gui.EnumWindows(self.__window_enum_callback, wildcard)

    def set_foreground(self):
        '''put the window in the forground'''
        win32gui.SetForegroundWindow(self._handle)