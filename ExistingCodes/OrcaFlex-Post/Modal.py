import logging
import math
import sys

import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt
from matplotlib import rc

rc('mathtext', default='regular')
import csv
import json

import numpy as np
import pandas as pd
from dataManager.customInputs import ExcelRead

from common.set_logging import setLogging
from common.ymlInput import ymlInput


def readFirstLine(FileName):
    with open(FileName) as f:
        line = f.readline()

    return line

# Data preparation
defaultYml = "dataManager\\modal.yml"
# Get updateYML file
try:
    if (sys.argv[1] != None):
        updateYml = "dataManager\\" + sys.argv[1]
        logging.critical("Updating default values with contents in file {0}" .format(updateYml) )
except:
    updateYml = None
    logging.critical("No update values file is provided. Running program default values")

# Get updated configuration file for Analysis
cfg = ymlInput(defaultYml, updateYml)
try:
    cfg['FileName'] = updateYml.split('\\')[1].split('.')[0]
except:
    cfg['FileName'] = defaultYml.split('\\')[1].split('.')[0]

# Set logging
setLogging(cfg['Default']['logLevel'])

ModesdfArray = []
for fileIndex in range(0, len(cfg['ModalReadingSets'])):
    customdata = {"FileName": cfg['ModalReadingSets'][fileIndex]['io']}

    FirstLine = readFirstLine(customdata['FileName'])
    FirstLineArray = FirstLine.split(' ')
    NoOfModes = int(FirstLineArray[0])
    NoOfNodes = int(FirstLineArray[1])
    print(FirstLine)

    customdata = {"FileName": cfg['ModalReadingSets'][fileIndex]['io']
                ,"skiprows": 1
                ,"skipfooter": NoOfNodes*NoOfModes
                ,"sep":" "
                ,"header": None
                ,"engine": "python"
                ,"Label": cfg['ModalReadingSets'][fileIndex]['Label']
                }

    df = pd.read_table(customdata['FileName'], sep=customdata["sep"], skiprows=customdata["skiprows"], skipfooter=customdata["skipfooter"], engine=customdata["engine"], header=customdata["header"])
    print(df.head())
    ModesSummaryDF = pd.DataFrame()
    ModesSummaryDF['Mode Number']= df[0]
    ModesSummaryDF['Frequency']= df[1]/2/math.pi

    df = pd.read_table(customdata['FileName'], sep=customdata["sep"], skiprows=customdata["skiprows"]+len(ModesSummaryDF), engine=customdata["engine"], header=customdata["header"])
    df.rename(columns={0: 'Mode Number', 1: 'Node Number', 2: 'Mode Shape', 3: 'Mode Slope', 4: 'Mode Curvature', 5: 'Mode Unknown'}, inplace=True)

    ModeCurvature = []
    ModeShape = []
    ModeSlope = []
    ModeUnknown = []
    for ModeNumber in range(1, NoOfModes + 1):
        ModeCurvature.append(df[df['Mode Number']==ModeNumber]['Mode Curvature'].max())
        ModeShape.append(df[df['Mode Number']==ModeNumber]['Mode Shape'].max())
        ModeSlope.append(df[df['Mode Number']==ModeNumber]['Mode Slope'].max())
        ModeUnknown.append(df[df['Mode Number']==ModeNumber]['Mode Unknown'].max())
    
    ModesSummaryDF['Mode Curvature'] = ModeCurvature
    ModesSummaryDF['Mode Shape'] = ModeShape
    ModesSummaryDF['Mode Slope'] = ModeSlope
    ModesSummaryDF['Mode Unknown'] = ModeUnknown

    print(df.head())
    print(ModesSummaryDF.head())
    ModesdfArray.append(ModesSummaryDF)


suptitle = cfg['PlotSettings']['PltSupTitle']
title = cfg['PlotSettings']['PltTitle']
plt.suptitle(suptitle)
plt.title(title)

for fileIndex in range(0, len(cfg['ModalReadingSets'])):
    x = ModesdfArray[fileIndex]['Frequency']
    y = ModesdfArray[fileIndex]['Mode Curvature']
    label = cfg['ModalReadingSets'][fileIndex]['Label']

    plt.plot(x,y, label=label)

xlabel = cfg['PlotSettings']['PltXLabel'][0]
ylabel = cfg['PlotSettings']['PltYLabel']
FileName = cfg['FileName']
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend()
plt.grid()
plt.savefig('results\\Plots\\' + FileName + 'Frequency', dpi=800)
plt.cla()
plt.clf()
plt.close()

plt.suptitle(suptitle)
plt.title(title)
for fileIndex in range(0, len(cfg['ModalReadingSets'])):
    x = ModesdfArray[fileIndex]['Mode Number']
    y = ModesdfArray[fileIndex]['Mode Curvature']
    label = cfg['ModalReadingSets'][fileIndex]['Label']

    plt.plot(x,y, label=label)

xlabel = cfg['PlotSettings']['PltXLabel'][1]
ylabel = cfg['PlotSettings']['PltYLabel']
FileName = cfg['FileName']
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend()
plt.grid()
plt.savefig('results\\Plots\\' + FileName + 'ModeNumber', dpi=800)
plt.close()
