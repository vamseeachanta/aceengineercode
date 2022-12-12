# -*- coding: utf-8 -*-
"""
Created on September 20 2018
"""
'''
Author: Vamsee Achanta
Date Updated: 2018-09-20
Objective: To generate catenary riser shape and evaluate static configuration
Run instructions with:
 Default yml file : python APISTD2RD.py
 Update default yml with parameters in 12.yml: python APISTD2RD.py 12.yml
 Outputs: JSON file and ASCII DataFrame with outputs

 UPDATES:
 Input YML: Relocate Spacing to PlotSettings
 Rename Summary "Hangoff" to "HangOffToSag"


'''
import logging
import math
import sys
from collections import OrderedDict
from math import *

import numpy as np
import oyaml as yaml
import pandas as pd
from API579Methods import API579GML, API579LML

from common.customInputs import ExcelRead
from common.DataFrame_To_Image import DataFrame_To_Image
from common.DataFrame_To_xlsx import DataFrameArray_To_xlsx_openpyxl
from common.plotContourf import plotContourf
from common.plotCustom import plotCustom
from common.saveData import saveDataFrame, saveDataJson, saveDataYaml
from common.set_logging import setLogging
# from catenarycalculation import *
from common.ymlInput import ymlInput

# Data preparation
defaultYml = "dataManager\\API579.yml"

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
logging.info(cfg)

if cfg['Default']['Analysis']['GML']['Circumference']:
    cfg['Result'] = {}
    cfg['Result']['Circumference'] = []
    for fileIndex in range(0, len(cfg['ReadingSets'])):
        customdata = {"io": cfg['ReadingSets'][fileIndex]['io'],
                        "sheet_name": cfg['ReadingSets'][fileIndex]['sheet_name'],
                        "skiprows": cfg['ReadingSets'][fileIndex]['skiprows'],
                        "skipfooter": cfg['ReadingSets'][fileIndex]['skipfooter'],
                        "index_col":  cfg['ReadingSets'][fileIndex]['index_col']
        }
        df = ExcelRead(customdata)
 
# Generate Heat Map
        customdata = { "Index_Name" : 'Length',
            "Columns_Name" : 'Circumference',
            "FileName" : 'results\\Plots\\' + cfg['ReadingSets'][fileIndex]['io'].split('\\')[1].split('.')[0] + '_' + cfg['ReadingSets'][fileIndex]['Label'],
            "PltSupTitle": cfg['PlotSettings']['Data']['PltSupTitle'],
            "PltTitle": cfg['PlotSettings']['Data']['PltTitle'] + ' '+ cfg['ReadingSets'][fileIndex]['Label'] + ', Tnom: {0} inch, Tmin: {1} inch' .format(cfg['Geometry']['DesignWT'], cfg['Geometry']['tmin']),
            "PltXLabel": cfg['PlotSettings']['Data']['PltXLabel'],
            "PltYLabel" : cfg['PlotSettings']['Data']['PltYLabel'],
            "PltLims" : cfg['ReadingSets'][fileIndex]['Contour'],
            # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
            "PltOrigin" : 'upper',
            "PltShowContourLines" : False,
            "DataFrameRowReversed" : True
            }
        # plotHeatMap(df, customdata)
        plotContourf(df, customdata)

        df = df*cfg['ReadingSets'][fileIndex]['DataCorrectionFactor']
        summary, GMLMAWPResults = API579GML(df, cfg, fileIndex)
        cfg['Result']['Circumference'].append(summary)

        GMLMAWPResultsDF = pd.DataFrame.from_dict(GMLMAWPResults)
        FileName = 'results\\data\\' + 'Summary_GML_'+ str(fileIndex) + '_' + cfg['FileName']
        print(FileName)
        Acceptable_FCA = np.interp(cfg['Design']['InternalPressure'], GMLMAWPResultsDF['MAWP'].iloc[::-1].values, GMLMAWPResultsDF['FCA'].iloc[::-1].values)
        print("Acceptable GML FCA is : {0}" .format(Acceptable_FCA))

        customdata = {"PltSupTitle": cfg['PlotSettings']['GML']['PltSupTitle'],
                "PltTitle": cfg['PlotSettings']['GML']['PltTitle'] + ', ' + cfg['ReadingSets'][fileIndex]['Label'],
                "PltXLabel": cfg['PlotSettings']['GML']['PltXLabel'],
                "PltYLabel" : cfg['PlotSettings']['GML']['PltYLabel'],
                'Label' : ['MAWP'],
                'PltColumns' : ['FCA', 'MAWP'],
                "YLim": [0, 5000],
                'Axhline' : [cfg['Design']['InternalPressure']],
                # 'Text': 'MAWP Reduced, Flaw dimension o: s={0} and c={1},  Min. Measured WT ={2}' .format(LMLSummaryDF.iloc[0]['s'], LMLSummaryDF.iloc[0]['c'], LMLSummaryDF.iloc[0]['tmm']),
                'TextFields': [{"x": 0.05, "y": 1200, "Text": " "}],
                'FileName': 'results\\Plots\\' + 'Summary_GML_'+ str(fileIndex) + '_' + cfg['FileName'] + '_PLT'+ '.png'
        }
        plotCustom(GMLMAWPResultsDF, customdata)


    FileName = 'results\\data\\' + 'Summary_GML_' + cfg['FileName']
    saveDataYaml(cfg, FileName)
    GMLSummaryDF = pd.DataFrame.from_dict(cfg['Result']['Circumference'])
    GMLSummaryDF = GMLSummaryDF.round(3)
    cols = ['Description', "Len (inch)", "Min WT (inch)", "Avg. WT (inch)", 'Corr. Rate (inch/year)', 'Rem. Life (yrs)', "Max WT (inch)"]
    GMLSummaryDF = GMLSummaryDF[cols]
    DataFrame_To_Image(GMLSummaryDF, FileName + '.png')

LMLSummaryDFArray = []
LMLFileNameArray = []
if cfg['Default']['Analysis']['LML']:
    for fileIndex in range(0, len(cfg['LML']['LTA'])):
        customdata = {"io": cfg['LML']['LTA'][fileIndex]['io'],
                        "sheet_name": cfg['LML']['LTA'][fileIndex]['sheet_name'],
                        "skiprows": cfg['LML']['LTA'][fileIndex]['skiprows'],
                        "skipfooter": cfg['LML']['LTA'][fileIndex]['skipfooter'],
                        "index_col":  cfg['LML']['LTA'][fileIndex]['index_col']
        }
        df = ExcelRead(customdata)
        df = df*cfg['LML']['LTA'][fileIndex]['DataCorrectionFactor']
        LMLResults = API579LML(df, cfg, fileIndex)
        LMLSummaryDF = pd.DataFrame.from_dict(LMLResults)
        FileName = 'results\\data\\' + 'Summary_LML_'+ str(fileIndex) + '_' + cfg['FileName']
        LMLFileNameArray.append('LML_'+ str(fileIndex) + '_')
        decimalArray = pd.Series([2, 2, 0, 0, 0, 0, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3], index=LMLSummaryDF.columns.values)
        LMLSummaryDF = LMLSummaryDF.round(decimalArray)
        LMLSummaryDFArray.append(LMLSummaryDF)
        DataFrame_To_Image(LMLSummaryDF, FileName + '_TBL' +'.png', col_width=1.0)
        # LMLSummaryDF.to_csv(FileName + '_TBL' +'.csv')
        # DataFrame_To_xlsx(LMLSummaryDF, customdata)
        print(FileName)
        Acceptable_FCA = np.interp(cfg['Design']['InternalPressure'], LMLSummaryDF['MAWPr, L2'].iloc[::-1].values, LMLSummaryDF['FCA'].iloc[::-1].values)
        print("Acceptable LML FCA is : {0}" .format(Acceptable_FCA))

        customdata = {"PltSupTitle": cfg['PlotSettings']['LML']['PltSupTitle'],
                "PltTitle": cfg['PlotSettings']['LML']['PltTitle'] + ', ' + cfg['LML']['LTA'][fileIndex]['Label'],
                "PltXLabel": cfg['PlotSettings']['LML']['PltXLabel'],
                "PltYLabel" : cfg['PlotSettings']['LML']['PltYLabel'],
                'Label' : ['MAWP, No Flaw', 'MAWP Reduced, L1', 'MAWP Reduced, L2'],
                'PltColumns' : ['FCA', 'MAWP', 'MAWPr, L1', 'MAWPr, L2'],
                "YLim": [0, 5000],
                'Axhline' : [cfg['Design']['InternalPressure']],
                # 'Text': 'MAWP Reduced, Flaw dimension o: s={0} and c={1},  Min. Measured WT ={2}' .format(LMLSummaryDF.iloc[0]['s'], LMLSummaryDF.iloc[0]['c'], LMLSummaryDF.iloc[0]['tmm']),
                'TextFields': [{"x": 0.05, "y": 1200, "Text": "MAWP Reduced"},
                        {"x": 0.05, "y": 1000, "Text": "Flaw dimension (inch): s={0} and c={1}" .format(LMLSummaryDF.iloc[0]['s'], LMLSummaryDF.iloc[0]['c'])},
                        {"x": 0.05, "y": 800, "Text": "Avg. Measured WT (inch) ={0}" .format(LMLSummaryDF.iloc[0]['tavg'])},
                        {"x": 0.05, "y": 600, "Text": "Min. Measured WT (inch)={0}" .format(LMLSummaryDF.iloc[0]['tmm'])},
                        {"x": 0.05, "y": 400, "Text": "FCA outsideFlaw = {0} times FCA flaw" .format(cfg['LML']['LTA'][fileIndex]['FCANonFlawRatio'])}
                ],
                'FileName': 'results\\Plots\\' + 'Summary_LML_'+ str(fileIndex) + '_' + cfg['FileName'] + '_PLT'+ '.png'
        }
        plotCustom(LMLSummaryDF, customdata)

#  For plot without the MAWP
        customdata = {"PltSupTitle": cfg['PlotSettings']['LML']['PltSupTitle'],
                "PltTitle": cfg['PlotSettings']['LML']['PltTitle'] + ', ' + cfg['LML']['LTA'][fileIndex]['Label'],
                "PltXLabel": cfg['PlotSettings']['LML']['PltXLabel'],
                "PltYLabel" : cfg['PlotSettings']['LML']['PltYLabel'],
                'Label' : ['MAWP Reduced, L1', 'MAWP Reduced, L2'],
                'PltColumns' : ['FCA', 'MAWPr, L1', 'MAWPr, L2'],
                "YLim": [0, 5000],
                'Axhline' : [cfg['Design']['InternalPressure']],
                # 'Text': 'MAWP Reduced, Flaw dimension o: s={0} and c={1},  Min. Measured WT ={2}' .format(LMLSummaryDF.iloc[0]['s'], LMLSummaryDF.iloc[0]['c'], LMLSummaryDF.iloc[0]['tmm']),
                'TextFields': [{"x": 0.05, "y": 1200, "Text": "MAWP Reduced"},
                        {"x": 0.05, "y": 1000, "Text": "Flaw dimension (inch): s={0} and c={1}" .format(LMLSummaryDF.iloc[0]['s'], LMLSummaryDF.iloc[0]['c'])},
                        {"x": 0.05, "y": 800, "Text": "Avg. Measured WT (inch) ={0}" .format(LMLSummaryDF.iloc[0]['tavg'])},
                        {"x": 0.05, "y": 600, "Text": "Min. Measured WT (inch)={0}" .format(LMLSummaryDF.iloc[0]['tmm'])},
                        {"x": 0.05, "y": 400, "Text": "FCA outsideFlaw = {0} times FCA flaw" .format(cfg['LML']['LTA'][fileIndex]['FCANonFlawRatio'])}
                ],
                'FileName': 'results\\Plots\\' + 'Summary_LML_'+ str(fileIndex) + '_' + cfg['FileName'] + '_PLT1'+ '.png'
        }
        plotCustom(LMLSummaryDF, customdata)

    #  Send LML Data to Excel Sheet
    customdata = {"FileName" : 'results\\data\\' + cfg['FileName'] + '.xlsx',
            "SheetNames": LMLFileNameArray,
            "thin_border" : True}
    DataFrameArray_To_xlsx_openpyxl(LMLSummaryDFArray, customdata)

if cfg['Default']['Analysis']['B31G']:
    for fileIndex in range(0, len(cfg['B31G'])):
        customdata = {"io": cfg['B31G'][fileIndex]['io'],
                        "sheet_name": cfg['B31G'][fileIndex]['sheet_name'],
                        "skiprows": cfg['B31G'][fileIndex]['skiprows'],
                        "skipfooter": cfg['B31G'][fileIndex]['skipfooter'],
                        "index_col":  cfg['B31G'][fileIndex]['index_col']
        }
        df = ExcelRead(customdata)
        df.replace(to_replace='No Limit', value=99, inplace=True)
        df.reset_index(level=0, inplace=True)
        df.columns = df.columns.map(str)

        customdata = {"PltSupTitle": cfg['PlotSettings']['B31G']['PltSupTitle'],
            "PltTitle": cfg['PlotSettings']['B31G']['PltTitle'] + ', ' + cfg['B31G'][fileIndex]['Label'],
            "PltXLabel": cfg['PlotSettings']['B31G']['PltXLabel'],
            "PltYLabel" : cfg['PlotSettings']['B31G']['PltYLabel'],
            'Label' : ['Pipe WT:' + str(x) for x in df.columns][1:len(df.columns)],
            'PltColumns' : [str(x) for x in df.columns],
            "YLim": [0, 20],
            'Axhline' : [cfg['B31G'][fileIndex]['LengthLimit']],
            # 'Text': 'MAWP Reduced, Flaw dimension o: s={0} and c={1},  Min. Measured WT ={2}' .format(LMLSummaryDF.iloc[0]['s'], LMLSummaryDF.iloc[0]['c'], LMLSummaryDF.iloc[0]['tmm']),
            'TextFields': [{"x": 0.05, "y": 1200, "Text": " "},
                    {"x": 0.05, "y": 1000, "Text": " "}
                    ],
            'FileName': 'results\\Plots\\' + 'B31G_'+ str(fileIndex) + '_' + cfg['FileName'] + '_PLT'+ '.png'
        }

        plotCustom(df, customdata)
        
