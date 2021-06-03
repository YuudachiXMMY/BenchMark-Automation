# [_sysUtils.py_](/lib/utils.py)

#### Modules Utilized

##### External modules:
`os`, `sys`, `re`, `subprocess`, `json`, `logging`

##### Local modules:
`lib.logger`

## `searchFile(pathname, filename)`

Return all matched files under a specific path.

#### Parameter:
1. `pathname` - a specific path to search for.
2. `filename` - a filename to search for (Regular Expression can be used).

#### Return:
- A list of sting representing all matched file names

## `killProgress(process)`

A function call a terminal and utilize CMD command to kill a progress.

#### Parameter:
1. `process` - a process to be forced to kill.

#### Return:
- `non-Zero` - succeed to call the terminal for killing the process.
- `0` - failed to open the terminal.
- `-1` - EXCEPTION occurred.

## `read_json(file)`

Read a .json file and return a json type.

#### Parameter:
1. `file` - a filename to be read as .json data.

#### Return:
- A Python's Data Object representing the data in the .json file.
- `None` - EXCEPTION occurred.

## `write_json(file, data, tar=None)`

Over-write the .json file with input data.

#### Parameter:
- `file` - a filename to be write.
- `data` - data to write in the .json file

#### Return:
- `1` - Succeed Over-Write
- `-1` - EXCEPTION occurred.

## `monitoring()`

**[NOT IN USED]** A small tool that can detect system RAM

## `printAll(data)`

Print everything in the data Object. Should only used inside the ProgramInfo Object

## `detectCrashDumps(tar="MEMORY.DMP")`

Detect whether the window's dump is generated under _%LOCALAPPDATA%\CrashDumps_

#### Parameter:
- `tar` - the target path to copy to (default to _C:\WinDumps_)

#### Return:
- `True` - The dump file is detected
- `False` - otherwise, the file is not detected