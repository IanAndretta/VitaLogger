from time import strftime
from os import listdir, makedirs, remove
from zipfile import ZipFile, ZIP_DEFLATED

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
        del codes

class Logger():
    ERROR = LoggerLevel(name="ERROR", color="\033[31m")
    WARN = LoggerLevel(name="WARN", color="\033[33m")
    INFO = LoggerLevel(name="INFO", color="\033[32m")

    def __init__(self, logger_folder : str, include_time : bool = True, include_level : bool = True, compress_files = True):
        self.logger_folder = logger_folder
        self.include_time = include_time
        self.include_level = include_level
        self.compress_files = compress_files

        self.use_log_folder = True
        self.time_format = strftime("%H:%M:%S")
        self.reset_color = "\033[0m"
        self.print_to_console = True
        self.log_name = "/log"

        #Creates a log folder if its gone
        if self.use_log_folder:
            try: 
                makedirs(logger_folder)
                print(f"Created a log folder at {self.logger_folder}")
            except FileExistsError: pass
            log_version = self.getLogVersion()

            #Compress the old log
            if self.compress_files and log_version > 0:
                try:
                    with ZipFile(self.logger_folder + self.log_name + str(log_version-1) + ".zip", "w", ZIP_DEFLATED) as zf:
                        zf.write(self.logger_folder + self.log_name + str(log_version-1) + ".log", compress_type=ZIP_DEFLATED)

                    #Delete old log
                    remove(self.logger_folder + self.log_name + str(log_version-1) + ".log")
                except FileNotFoundError: pass

            #Creates a log with correct version number
            self.increaseLogVersion()
            with open(self.logger_folder + self.log_name + str(log_version) + ".log", "a") as file:
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
            with open(self.logger_folder + self.log_name + str(self.getLogVersion()-1) + ".log", "a") as file:
                file.write(output.replace(logger_level.color, "").replace(self.reset_color, "") + "\n")


    def getLogVersion(self) -> int:
        version_number = None

        try:
            with open(self.logger_folder + "/logversion", "r") as file:
                contents = int(file.read())
                if contents.bit_count == 0: version_number = 0
                else: version_number = contents
        except FileNotFoundError:
            with open(self.logger_folder + "/logversion", "w") as file: 
                file.write("0")
                version_number = 0

        return version_number


    def increaseLogVersion(self):
        current_version = self.getLogVersion()
        with open(self.logger_folder + "/logversion", "w") as file:
            file.write(str(current_version + 1))
