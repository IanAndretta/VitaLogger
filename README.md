Plain Logger is a simple logger library for python
Install at https://pypi.org/project/vitalogger/

Example:
logger = Logger(logger_folder="my_logs_folder", include_time = True, include_level = True)
logger.log(msg="Cannot divided by zero", logger_level=Logger.ERROR)
[00:58:41] [ERROR] Cannot divided by zero

Logger Class Params:
logger_folder : string -> the name of the folder where the log files will be saved
include_time : boolean -> if time is included
included_level : boolean -> if the level is included for example [INFO] or [WARN]

Logger Class Methods:
log(msg, LoggerLevel)

The logger class includes 3 Built-in Logger Level:
ERROR
WARN
INFO

You can also make your own logger levels
success_level = LoggerLevel(name="SUCCESS", color="\033[1;32m\033[1m")
Logger.log(msg="Worked", LoggerLevel=success_level)


ANSI color codes for python:
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
