import datetime
import logging
import os


def writeRunTime(programStartTime):
    logging.critical('RunTime in HH:MM:SS is {0}' .format(datetime.datetime.now() - 
            programStartTime) )