# [_logger.py_](/lib/logger.py)

#### Modules Utilized

##### External modules:
`os`, `sys`, `logging`

## `logger(logName, dir='')`

Return a logger with name in format '%Y-%m-%d-%H.%M' under "./Logs/" folder

- format: `LogName.log`
- location: `./Logs/%Y-%m-%d-%H.%M`

- default Log output level: `WARNING`
- default Console output level: `WARNING`

#### Return:
- A logger for logging.
- `None` - EXCEPTION occurred.