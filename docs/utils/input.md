# [_input.py_](/lib/input.py)

#### Modules Utilized

##### External modules:
`os`, `sys`, `subprocess`, `re`, `time`, `random`, `win32api`, `win32con`, `pyautogui as pag`

##### Local modules:
`lib.logger`, `lib.VK_CODE`

## `key_input(key, t=0.05)`

Perform a key press down and press up action.

#### Parameter:
1. `key` - a key to be pressed.
2. `t` - time period in second between pressdown and pressup (default to 0.05).

#### Return:
- `1` - succeed in performing a key pressing process.
- `0` - failed to perform a key pressing process.

## `key_inputs(str_input='', t=0.05)`

Perform a serious of key pressdowns and pressups.

#### Parameter:
1. `str_input` - a string of keys to be pressed (default to '').
2. `t` - time period in second between each key to be pressed (default to 0.05).

## `key_enter(t=0.5)`

Perform a key action of ENTER.

#### Parameter:
1. `t` - time period in second between pressdown and pressup (default to 0.05).

## `key_space(t=0.5)`

Perform a key action of ENTER.

#### Parameter:
1. `t` - time period in second between pressdown and pressup (default to 0.05).

## `key_alt_tab(t=0.5)`

Perform a key action of ALT + TAB.

#### Parameter:
1. `t` - time period in second between pressdown and pressup (default to 0.05).

## `key_alt_f4()`

Perform a key action of ALT + TAB.

#### Parameter:
1. `t` - time period in second between pressdown and pressup (default to 0.05).

## `clickLeft(x, y, duration=0)`

Perform a mouse action of left clicking on screen position at (x, y).

#### Parameter:
1. `x` - horizontal position to be clicked.
2. `y` - vertical position to be clicked.

## `clickRight(x=0, y=0, duration=0)`

Perform a mouse action of right clicking on screen position at (x, y).

#### Parameter:
1. `x` - horizontal position to be clicked.
2. `y` - vertical position to be clicked.

## `move(start_x, start_y, dest_x, dest_y, duration=0)`

Perform a mouse action to move the mouse from `(start_x, start_y)` to `(dest_x, dest_y)` in duration time.

#### Parameter:
1. `start_x` - horizontal position to start
2. `start_y` - vertical position to start
3. `dest_x` - horizontal position to end
4. `dest_y` - vertical position to end
5. `duration` - action's duration in seconds

## `moveTo(dest_x, dest_y, duration=0)`

Perform a mouse action of clicking on screen position at (x, y).

#### Parameter:
1. `x` - horizontal position to be clicked.
2. `y` - vertical position to be clicked.

## `getMouse(t=0)`

Get the mouse position and print in the console

#### Parameter:
1. `t` - period to get the mouse position

#### Return:
- `(x, y)` - a tuple which x represent the x-position of the mouse and y represent the y-position of the mouse.

## `getMouseLogging(t=0)`

Get the mouse position and print in the console only when the mouse position changes

#### Parameter:
1. `t` - period to get the mouse position

#### Return:
- `(x, y)` - a tuple which x represent the x-position of the mouse and y represent the y-position of the mouse.