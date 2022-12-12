# -*- coding: utf-8 -*-
"""
Created on September 20 2018
"""
'''
Author: Vamsee Achanta
Date Updated: 2018-09-20
Objective: To summarize ASME31.8 results
Run instructions with:
 Default yml file : python ASME.py

 UPDATES: 
 Input YML: Relocate Spacing to PlotSettings
 Rename Summary "Hangoff" to "HangOffToSag"

'''
import logging
import math
import sys
from math import *

import matplotlib.pyplot as plt

from common.setLogging import setLogging
from custom.ASMEB31.extractData import extractData
from custom.ASMEB31.fileList import fileList
from dataManager.ASMEB31.ymlInput import ymlInput
from results.ASMEB31.plotCustom import plotCustom
#from extractData import extractPlotData
from results.ASMEB31.saveData import saveDataFrame

# Data preparation
defaultYml = "dataManager\\ASMEB31\\ASMESummary.yml"
# Get updateYML file
try:
    if (sys.argv[1] != None):
        updateYml = "dataManager\\ASMEB31\\" + sys.argv[1]
        logging.critical("Updating default values with contents in file {0}" .format(updateYml))
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
setLogging(cfg['default']['logLevel'])

# Get file List

fileList = []
for fileIndex in range(0, len(cfg['ymlFiles'])):
    fileList.append(cfg['ymlFiles'][fileIndex]['io'])

# Get data
dataDF = extractData(fileList, cfg)
# Save Data
fileName = cfg['dataFrame']['label']
saveDataFrame(dataDF, fileName)




## Get plot data
customdata = {"PltSupTitle": cfg['PlotSettings']['Data']['PltSupTitle'],
        "PltTitle": cfg['PlotSettings']['Data']['PltTitle'] + ', ' + cfg['ymlFiles'][fileIndex]['Label'],
        "PltXLabel": cfg['PlotSettings']['Data']['PltXLabel'],
        "PltYLabel" : cfg['PlotSettings']['Data']['PltYLabel'],
        'Label' : ['MAOP'],
        'PltColumns' : ['D/tMinimum Ratio', 'MAOP'],
        "YLim": [0, 5000],
      #  'Axhline' : [cfg['Design']['InternalPressure']],
        # 'Text': 'MAWP Reduced, Flaw dimension o: s={0} and c={1},  Min. Measured WT ={2}' .format(LMLSummaryDF.iloc[0]['s'], LMLSummaryDF.iloc[0]['c'], LMLSummaryDF.iloc[0]['tmm']),
        'TextFields': [{"x": 0.05, "y": 1200, "Text": " "}],
        'FileName': 'results\\ASMEB31\\Plots\\' + 'Summary_Code_'+ str(fileIndex) + '_' + cfg['FileName'] + '_PLT'+ '.png'
}
plotCustom(dataDF,customdata)

