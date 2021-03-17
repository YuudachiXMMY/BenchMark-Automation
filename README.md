# BenchMark-Automation

[![Latest Release - Downloads](https://img.shields.io/github/downloads/YuudachiXMMY/BenchMark-Automation/03_17_2021_1/total)](https://github.com/YuudachiXMMY/BenchMark-Automation/releases)

## Release

### Latest
Download: [Build.7z](https://github.com/YuudachiXMMY/BenchMark-Automation/releases/download/03_01_2021_1/Build.7z)


## How to use this program:

### Pre-Requisite
1. Make sure you've installed the latest *Python 3*;
2. Make sure *Python 3* and pip have been added to the system environment.

### Unpacking:
I recommend using 7zip to extract the main contents of this program.

### Run program:
1. Edit `config.json` using any text editor ;
2. Run `man.exe` as **administrator**;
3. Follow the instructions in the program and have fun :)


## Source-Code Usage

### _main.py_

#### `initializeProgram()`

Set the *global variable* `PROGRAM` by constructing a [ProgramInfo](./main/ProgramInfo.py).

#### `startScripts()`
Get the current game's run list and loop times from `PROGRAM` and call functions to run the scripts.

### _m.py_

Entirely Same As _main.py_. Is used to build and generate releases.

### ./lib/*

#### _input.py_

***Please check detailed specification in the original module file.***

A module that implements mouse and keyboard actions in _Windows System_.

#### _keyboardUtils.py_

***Please check detailed specification in the original module file.***

A module that implements common mouse and keyboard actions. It also contains methods to perform _normal Benchmarking_, _stressed Benchmarking_, and _random Character Controlling_.

#### _logger.py_

***Please check detailed specification in the original module file.***

A module that construct and return a [logging](https://docs.python.org/3.5/library/logging.html) Object that can be used to debug and log information during runtime.

#### _screen.py_

***Please check detailed specification in the original module file.***

A module that can take and save screenshots and also find whether a window is opened in _Windows System_.

#### _utils.py_

***Please check detailed specification in the original module file.***

A module that can read and write JSON files, search files, and force to kill a process in _Windows System_.

#### _VK_CODE.py_

***Please check detailed specification in the original module file.***

A class having two dictionaries to represent VK_CODE. Mainly used for [_input.py_](./lib/input.py).

### ./main/*

#### _ProgramInfo.py_

***Please check detailed specification in the original module file.***

A class that shows this program interact-able screen and save all the user config settings.

#### _programText_cn.json_

A JSON file that perform the Chinese language for the program interact-able screen.
