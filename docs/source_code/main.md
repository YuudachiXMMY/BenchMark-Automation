# Source Code Documentation

## [_main.py_](/main.py)

Work as the main program, calling all other modules to work together.

#### Modules Utilized

##### External modules:
`os`, `sys`, `subprocess`, `re`, `time`, `random`,
`win32gui`, `win32api`, `win32con`, `pyautogui as pag`

##### Local modules:
`lib.logger`, `lib.VK_CODE`

#### Functions

### `CMDParam()`

**TODO:** Parse parameters directly from Command Line and read them as the local variable.

### `initializeProgram()`

Set the _global variable_ `PROGRAM` by constructing a [ProgramInfo](./main/ProgramInfo.py) object.

### `startScripts()`

Get the current game's run list and loop times from `PROGRAM` and call functions to start scripts.

## [_m.py_](/m.py)

Entirely the same as _main.py_. Is used to build and generate releases.

# ./lib/*

***Please check detailed specification in the original module file.***

## [_input.py_](/docs/source_code/lib/input.md)

A module that implements mouse and keyboard actions in _Windows System_.

## [_keyboardUtils.py_](/docs/source_code/lib/keyboardUtils.md)

A module that implements common mouse and keyboard actions. It also contains methods to perform _normal Benchmarking_, _stressed Benchmarking_, and _random Character Controlling_.

## [_logger.py_](/docs/source_code/lib/logger.md)

A module that construct and return a [logging](https://docs.python.org/3.5/library/logging.html) Object that can be used to debug and log information during runtime.

## [_screen.py_](/docs/source_code/lib/screen.md)

A module that can take and save screenshots and also find whether a window is opened in _Windows System_.

## [_utils.py_](/docs/source_code/lib/utils.md)

A module that can read and write JSON files, search files, and force to kill a process in _Windows System_.

## [_VK_CODE.py_](/docs/source_code/lib/VK_CODE.md)

A class having two dictionaries to represent VK_CODE. Mainly used for [_input.py_](./lib/input.py).

# ./main/*

***Please check detailed specification in the original module file.***

## [_ProgramInfo.py_](/docs/source_code/main/ProgramInfo.md)

A class that shows this program interact-able screen and save all the user config settings.

## _programText_cn.json_

A JSON file that perform the Chinese language for the program interact-able screen.
