from time import strftime
from os import listdir, makedirs

class LoggerLevel():
    def __init__(self, name : str, color : str):
        self.name = name
        self.color = color

    def ansi_color_codes():
        codes = r"""
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
"""
        print(codes)

class Logger():
    ERROR = LoggerLevel(name="ERROR", color="\033[31m")
    WARN = LoggerLevel(name="WARN", color="\033[33m")
    INFO = LoggerLevel(name="INFO", color="\033[32m")
    
    def __init__(self, logger_folder : str, include_time : bool = True, include_level : bool = True):
        self.logger_folder = logger_folder
        self.include_time = include_time
        self.include_level = include_level

        self.use_log_folder = True
        self.time_format = strftime("%H:%M:%S")
        self.reset_color = "\033[0m"
        self.print_to_console = True
        
        #Creates a log folder if its gone
        if self.use_log_folder:
            print(f"Creating log folder at {self.logger_folder}")
            try: makedirs(logger_folder)
            except FileExistsError: pass
        
            #Creates a log with correct version number
            with open(self.logger_folder + "/log" + str(len(listdir(self.logger_folder))) + ".log", "a") as file:
                file.write(f"[{self.time_format}] [INFO] Log Created\n")
    
    
    def log(self, msg : str, logger_level : LoggerLevel):
        output = ""
        
        if self.include_time: 
            output += f"{logger_level.color}[{self.time_format}] "
        
        if self.include_level: 
            output += f"{logger_level.color}[{logger_level.name}] "

        #Appends the message to the output
        output += logger_level.color + msg + self.reset_color
        if self.print_to_console: print(output)
        
        #Appends the output to the log.txt
        if self.use_log_folder:
            with open(self.logger_folder + "/log" + str(len(listdir(self.logger_folder)) -1) + ".log", "a") as file:
                file.write(output.replace(logger_level.color, "").replace(self.reset_color, "") + "\n")