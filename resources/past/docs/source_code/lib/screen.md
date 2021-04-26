# [_screen.py_](/lib/screen.py)

#### Modules Utilized

##### External modules:
`os`, `sys`, `re`, `subprocess`, `time`, `random`,
`win32gui`, `win32api`, `win32con`, `PIL.ImageGrab`

##### Local modules:
`lib.logger`

## `makescreenshot()`

Make a screenshot of the current Windows screen.

#### Return:
- A ImageGrab Object representing the current Windows screenshot.
- `None` - EXCEPTION occurred.

## `savescreenshot(task, error='')`

Save a screenshot under "./errors." folder.

#### Parameter:
1. `task` - the current task that is running.
2. `error` - error message (default to '').

#### Return:
- A string representing the screenshot file name.
- `None` - EXCEPTION occurred.

## `findWindow(windowName)`

Find a displayed window in 15 second with 5 tries.

#### Parameter:
1. `windowName` - a windows to be found displayed.

#### Return:
- `non-Zero` - representing the window's HD.
- `0` - failed to find the window and will save a screenshot.
- `None` - EXCEPTION occurred.

## `changeDisplayDirection(deviceIndex, angle)`

Rotate the Display Screen's Direction

#### Parameter:
1. `deviceIndex` - display device index
2. `angle` - angle to be rotated

#### Return:
- `True` - succeed in rotating the screen.
- `False` - failed to rotate the screen.

## `hasDisplayDevice(deviceIndex)`

 Check whether the screen device represented by the index is connected

#### Parameter:
- `deviceIndex` - the index representing a screen monitor

#### Return:
- `True` - the index is valid the screen monitor exist
- `False`
