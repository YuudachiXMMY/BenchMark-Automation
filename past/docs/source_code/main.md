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

Entirely the same as [_main.py_](/main.py). Is used to build and generate releases.

----

# ./lib/*

***Please check detailed specification in the original module file.***

## [_input.py_](/docs/source_code/lib/input.md)

A module that implements mouse and keyboard actions in _Windows System_.

## [_keyboardUtils.py_](/docs/source_code/lib/keyboardUtils.md)

A module that implements common mouse and keyboard actions. It also contains methods to perform _normal Benchmarking_, _stressed Benchmarking_, and _random Character Controlling_.

## [_logger.py_](/docs/source_code/lib/logger.md)

A module that construct and return a [_logging_](https://docs.python.org/3.5/library/logging.html) Object that can be used to debug and log information during runtime.

## [_screen.py_](/docs/source_code/lib/screen.md)

A module that can take and save screenshots and also find whether a window is opened in _Windows System_.

## [_utils.py_](/docs/source_code/lib/utils.md)

A module that can read and write JSON files, search files, and force to kill a process in _Windows System_.

## [_VK_CODE.py_](/docs/source_code/lib/VK_CODE.md)

A class having two dictionaries to represent VK_CODE. Mainly used for [_input.py_](/lib/input.py).

----

# ./main/*

***Please check detailed specification in the original module file.***

## [_ProgramInfo.py_](/docs/source_code/main/ProgramInfo.md)

A class that shows this program interact-able screen and save all the user config settings.

## [scripts/*](/main/scripts/)

Individual automation scripts to be ran.

----

# ./resources/*

## [config_settings/*](/docs/source_code/main/config_settings.md)

Game's configuration files. Mainly used to change graphic and other in-game settings by directly calling the `.reg` registration files.

## [environments/*](/docs/source_code/main/environments.md)

Required system environments that should be installed.

## [keyassist/*](/docs/source_code/main/keyassist.md)

Executor Programs of assisting keyboard and mouse actions generated by [***TinyTask***](https://sites.google.com/view/tinytask/)

## [office/*](/docs/source_code/main/office.md)

Office documents to be open for Office Automation Testing

## [saves/*](/docs/source_code/main/saves.md)

Game's save files for Benchmarking or other purposes.

## [tl/*](/docs/source_code/main/tl.md)

JSON files for Localization

----

# Localization

## Chinese

[***programText_cn.json***](/resources/tl/programText_cn.json)

A JSON file that perform the Chinese language for the program interact-able screen.

## English

[***programText_en.json***](/resources/tl/programText_en.json)

A JSON file that perform the English language for the program interact-able screen.