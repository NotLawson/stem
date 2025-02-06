### BetterLog ###
## IMPORTS ##
import time
from datetime import datetime

DEBUG = False

# create log file
try:
    open("log.txt", "r")
except:
    open("log.txt", "x")

## COLOURS DEFINE ##
class colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    DEBUG = '\033[32m'

## ERROR CLASS ##
# for people who use VSCode auto complete lol
class level:
    done = "DONE"
    warn = "WARNING"
    info = "INFO"
    error = "ERROR"
    fail = "FAIL"
    exit = "EXIT"
    debug = "DEBUG"

## LOG ##
def log(message, error_level=level.info):
    if error_level=="DONE":
        colour = colours.OKGREEN
    elif error_level=="WARNING":
        colour = colours.WARNING
    elif error_level=="INFO":
        colour = colours.OKCYAN
    elif error_level=="ERROR" or "FAIL" or "EXIT":
        colour = colours.FAIL
    elif error_level=="DEBUG":
        colour = colours.DEBUG
    
    coloured_message=f"{datetime.now().strftime('%H:%M:%S')} -- ({colour}{error_level}{colours.ENDC}) {colour}{message}{colours.ENDC}"
    print(coloured_message)

    normal_message=f"{datetime.now().strftime('%H:%M:%S')} -- ({error_level}) {message}"
    mod=open("log.txt","a")
    mod.write(normal_message+"\n")

## ASK ##
def ask(message):
    error_level = "INPUT"
    colour = colours.OKBLUE

    coloured_message=f"{datetime.now().strftime('%H:%M:%S')} -- ({colour}{error_level}{colours.ENDC}) {colour}{message}{colours.ENDC}\n"
    answer=input(coloured_message)

    normal_message=f"{datetime.now().strftime('%H:%M:%S')} -- ({error_level}) {message}\n{answer}"
    mod=open("log.txt","a")
    mod.write(normal_message+"\n")
    return answer


# levels
def info(message):
    log(message, level.info)
def done(message):
    log(message, level.done)
def warn(message):
    log(message, level.warn)
def error(message):
    log(message, level.error)
def fail(message):
    log(message, level.fail)
def exit(message):
    log(message, level.exit)
def debug(message):
    if DEBUG:
        log(message, level.debug)