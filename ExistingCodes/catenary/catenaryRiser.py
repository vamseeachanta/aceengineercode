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
import sys

from catenaryMethods import (buoyancyProperties, catenaryEquation,
                             catenaryForces, lazyWaveCatenaryEquation,
                             lazyWavePlot)
from dataManager.customUpdate import customUpdate
from dataManager.ymlInput import ymlInput
from logs.setLogging import setLogging
from orcaflexModel import WriteOrcaflexModel, orcaflexModel
from pipeProperties import pipeProperties
from results.saveData import saveDataFrame, saveDataJson, saveDataYaml


def BuildModel(FEAType):
    if cfg['default']['Analysis']['SLWR']:
        for LoadingIndex in range (0, len(cfg['EnvironmentLoad'][FEAType])):
            cfg['fileName'] = 'results\\FEA\\' + FEAType + '\\' + 'SLWR_' + cfg['FileName'] + '_' + cfg['EnvironmentLoad'][FEAType][LoadingIndex]['Wave']['WaveTrains'][0]['Name'] + '.yml'
            if cfg['default']['Analysis'][FEAType] == True:
                FEAmodel1, FEAmodel2 = orcaflexModel(cfg, FEAType, LoadingIndex)
                if FEAType == 'Extreme':
                    WriteOrcaflexModel([FEAmodel1, 'dataManager\\VesselTypes_Extreme.yml', FEAmodel2], cfg, FEAType, LoadingIndex)
                elif FEAType == 'Fatigue':
                    WriteOrcaflexModel([FEAmodel1, 'dataManager\\VesselTypes_Fatigue.yml', FEAmodel2], cfg, FEAType, LoadingIndex)

        saveDataYaml(cfg, 'results\\' + 'SLWR_' + 'Summary_' + cfg['FileName'], False)

    if cfg['default']['Analysis']['SCR']:
        for LoadingIndex in range (0, len(cfg['EnvironmentLoad'][FEAType])):
            cfg['fileName'] = 'results\\FEA\\' + FEAType + '\\' + 'SCR_' + cfg['FileName'] + '_' + cfg['EnvironmentLoad'][FEAType][LoadingIndex]['Wave']['WaveTrains'][0]['Name'] + '.yml'
            if cfg['default']['Analysis'][FEAType] == True:
                FEAmodel1, FEAmodel2 = orcaflexModel(cfg, FEAType, LoadingIndex)
                if FEAType == 'Extreme':
                    WriteOrcaflexModel([FEAmodel1, 'dataManager\\VesselTypes_Extreme.yml', FEAmodel2], cfg, FEAType, LoadingIndex)
                elif FEAType == 'Fatigue':
                    WriteOrcaflexModel([FEAmodel1, 'dataManager\\VesselTypes_Fatigue.yml', FEAmodel2], cfg, FEAType, LoadingIndex)


        saveDataYaml(cfg, 'results\\' + 'SCR_' + 'Summary_' + cfg['FileName'])

# Data preparation
defaultYml = "dataManager\\catenary.yml"
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

cfg = customUpdate(cfg)

# Set logging
setLogging(cfg['default']['logLevel'])

# Evaluate section properties and mass per unit length and related properties.

inputData = {"d": cfg["simpleCatenaryDefinition"]["verticalDistance"],
            "F": cfg["simpleCatenaryDefinition"]["axialLineForce"],
            "q" : cfg["simpleCatenaryDefinition"]["declinationAngle"]
            }

catenaryResult = catenaryEquation(inputData)
cfg['catenaryResult'] = catenaryResult

cfg = pipeProperties(cfg, FluidDensity=cfg['Material']['Fluid']['Rho'], Buoyancy = False)
WeightPerUnitLengthWithOutBuoyancy = cfg['equivalentPipe']['weightPerUnitLength']
inputData = {'weightPerUnitLength' : cfg['equivalentPipe']['weightPerUnitLength'],
            'S' : cfg['catenaryResult']['S'],
            'q' : cfg['catenaryResult']['q']
             }
output = catenaryForces(inputData)
cfg['catenaryResult']['FluidFilled'] = output

cfg = pipeProperties(cfg, FluidDensity=cfg['Material']['SeaWater']['Rho'], Buoyancy = False)

inputData = {'weightPerUnitLength' : cfg['equivalentPipe']['weightPerUnitLength'],
            'S' : cfg['catenaryResult']['S'],
            'q' : cfg['catenaryResult']['q']
             }
output = catenaryForces(inputData)
cfg['catenaryResult']['SeaWaterFilled'] = output

cfg = pipeProperties(cfg, FluidDensity=0, Buoyancy = False)
inputData = {'weightPerUnitLength' : cfg['equivalentPipe']['weightPerUnitLength'],
            'S' : cfg['catenaryResult']['S'],
            'q' : cfg['catenaryResult']['q']
             }
output = catenaryForces(inputData)
cfg['catenaryResult']['Empty'] = output

# Lazy Wave Analysis
cfg = buoyancyProperties(cfg)

lazyWaveInputs = {"WeightPerUnitLengthWithBuoyancy": cfg['lazyWaveCatenaryResult']['WeightPerUnitLengthWithBuoyancy'],
                "WeightPerUnitLengthWithOutBuoyancy": cfg['lazyWaveCatenaryResult']['WeightPerUnitLengthWithOutBuoyancy'],
                "SagBendElevationAboveSeabed": cfg['LazyWaveCatenaryDefinition']['SagBendElevationAboveSeabed'],
                "HogBendAboveSeabed": cfg['LazyWaveCatenaryDefinition']['HogBendAboveSeabed'],
               "HangOff": {"d": cfg['LazyWaveCatenaryDefinition']['VerticalDistance'] - cfg['LazyWaveCatenaryDefinition']['SagBendElevationAboveSeabed'],
            "q": cfg["LazyWaveCatenaryDefinition"]["declinationAngle"], "F": None     },
             }

#  For Benchmarking/Verification
# lazyWaveInputs = {"WeightPerUnitLengthWithBuoyancy" :  -1251.946261,
#                 "WeightPerUnitLengthWithOutBuoyancy" :  981.97,
#                 "SagBendElevationAboveSeabed" : cfg['LazyWaveCatenaryDefinition']['SagBendElevationAboveSeabed'],
#                 "HogBendAboveSeabed" : cfg['LazyWaveCatenaryDefinition']['HogBendAboveSeabed'],
#                "HangOff" :    {"d" : cfg['LazyWaveCatenaryDefinition']['VerticalDistance'] - cfg['LazyWaveCatenaryDefinition']['SagBendElevationAboveSeabed'],
#             "q" : cfg["LazyWaveCatenaryDefinition"]["declinationAngle"], "F": None     },
#                   "WeightPerUnitLength" :  cfg['equivalentPipe']['weightPerUnitLength']
#              }

cfg['lazyWaveCatenaryResult'].update(lazyWaveCatenaryEquation(lazyWaveInputs))
cfg['lazyWaveCatenaryResult']['TotalBuoyancy'] = (cfg['lazyWaveCatenaryResult']['WeightPerUnitLengthWithBuoyancy'] - cfg['lazyWaveCatenaryResult']['WeightPerUnitLengthWithOutBuoyancy'])*cfg['lazyWaveCatenaryResult']['Summary']['Buoyancy']['S']
cfg = lazyWavePlot(cfg, cfg['LazyWaveCatenaryDefinition']['Spacing'])

# Construct FEA Model
cfg = pipeProperties(cfg, FluidDensity=0, Buoyancy = False)
cfg['MainPipe'] = {'SteelSection': cfg['SteelSection'], 'BuoyancySection': cfg['BuoyancySection'],
        'InsulationSection': cfg['InsulationSection'], 'equivalentPipe': cfg['equivalentPipe']}
cfg = pipeProperties(cfg, FluidDensity=0, Buoyancy = True)
cfg['BuoyPipe'] = {'SteelSection': cfg['SteelSection'], 'BuoyancySection': cfg['BuoyancySection'],
        'InsulationSection': cfg['InsulationSection'], 'equivalentPipe': cfg['equivalentPipe']}

if cfg['default']['Analysis']['Extreme']:
    FEAType = 'Extreme'
    BuildModel(FEAType)
if cfg['default']['Analysis']['Fatigue']:
    FEAType = 'Fatigue'
    BuildModel(FEAType)

