# [_keyboardUtils.py_](/lib/keyboardUtils.py)

#### Modules Utilized

##### External modules:
`os`, `sys`, `time`, `random`,
`win32api`

##### Local modules:
`lib.input`, `lib.logger`, `lib.VK_CODE`

## `normBenchmarking(duration)`

Perform a key press down and press up action.

#### Parameter:
1. `duration` - a key to be pressed.

#### Return:
- `1` - succeed in performing a key pressing process.
- `0` - failed to perform a key pressing process.

## `stressBenchmarking(duration)`

Perform a stressed Benchmarking. Randomly performing an ALT+TAB action.

#### Parameter:
1. `duration`: duration to perform the stressed benchmarking

## `randomCharacterControl(duration)`

Perform a random Character Control for games.

1. `duration`: duration to perform the random character control


## `randomTyping(duration)`

Perform a random Typing Words for Office.

#### Parameter:
1. `duration`: duration to perform the random typing

## `randomRotate(duration)`

Perform a random screen rotating

#### Parameter:
1. `duration`: duration to perform the random screen rotating

## `mouseCharacterControl(action, keyTime)`

A method called by randomCharacterControl() to perform mouse control for characters.

#### Parameter:
1. `action`: action to perform
2. `keyTime`: duration to perform the key time

## `keyCharacterControl(action, keyTime)`

A method called by randomCharacterControl() to perform keyboard control for characters.

#### Parameter:
1. `action`: action to perform
2. `keyTime`: duration to perform the key time

## `callTinyTask(TinyTaskFile)`

Calling the .exe file under _./resources/tinytask/_ folder made by TinyTask

#### Parameter:
1. `TinyTaskFile`: a TinyTask File Name to be performed

#### Return:
- `0` - failed
- `1` - succeed

## `tinytask_resetMouse()`

Reset the mouse position to top-left, by calling _./resources/tinytask/mouse/reset_mouse.exe_ file made by TinyTask

#### Return:
- `0` - failed
- `1` - succeed