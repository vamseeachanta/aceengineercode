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
from math import *

import oyaml as yaml

from common.set_logging import setLogging
from custom.ASMEB31.ASMEMethods import *
#import ruamel.yaml
from custom.ASMEB31.temperatureDerating import temperatureDerating
from dataManager.ASMEB31.ymlInput import ymlInput
from results.ASMEB31.saveData import saveDataYaml

# Data preparation
defaultYml = "dataManager\\ASMEB31\\B31.yml"

# Get updateYML file
try:
    if (sys.argv[1] != None):
        updateYml = "dataManager\\ASMEB31\\" + sys.argv[1]
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

customdata = {"Code": cfg['Default']['Analysis']['Code']}
customdata = temperatureDerating(customdata)
cfg['Result'] = {"TemperatureDerating": customdata['TemperatureDerating']}

customdata = {"S": cfg['Material']['SMYS'], 
            "t" : cfg['Geometry']['DesignWT'],
            "D" : cfg['Geometry']['NominalOD'],
            "Pi": cfg['Design']['InternalPressure'],
            "Po": cfg['Design']['ExternalPressure'],
            "F" : cfg['DesignFactors']['Pressure'],
            "WeldFactor" : cfg['Material']['WeldFactor']['Seamless'],
            "T" : cfg['Result']['TemperatureDerating']
}

if cfg['Default']['Analysis']['Code'] == "ASME B31.4":
    from custom.ASMEMethods import ASMEB314InternalPressure
    customdata = ASMEB314InternalPressure(customdata)
    cfg['Result']['ASMEB314'] = {}
    cfg['Result']['ASMEB314']['InternalPressure'] = customdata

if cfg['Default']['Analysis']['Code'] == "ASME B31.8":
    from custom.ASMEMethods import ASMEB318InternalPressure
    customdata = ASMEB318InternalPressure(customdata)
    cfg['Result']['ASMEB318'] = {}
    cfg['Result']['ASMEB318']['InternalPressure'] = customdata

customdata = {"S": cfg['Material']['SMYS'], 
            "t" : cfg['Geometry']['DesignWT'],
            "D" : cfg['Geometry']['NominalOD'],
            "Pi": cfg['Design']['InternalPressure'],
            "Po": cfg['Design']['ExternalPressure'],
            "M": cfg['Design']['BendingMoment'],
            "Fa": cfg['Design']['AxialForce'],
            "F" : cfg['DesignFactors']['Longitudinal'],
            "WeldFactor" : cfg['Material']['WeldFactor']['Seamless'],
            "E" : cfg['Material']['E'],
            "Poissionsratio" : cfg['Material']['Poissionsratio'],
            "T" : cfg['Result']['TemperatureDerating'],
            "Alpha" : cfg['Material']['ThermalExpansionCoefficient'],
            "T1": cfg['Design']['Temperature']['Operating'],
            "T2": cfg['Design']['Temperature']['Ambient'],
            "Condition": cfg['Design']['Condition']
}

if cfg['Default']['Analysis']['Code'] == "ASME B31.4":
    from custom.ASMEMethods import ASMEB314LogitudinalStress
    customdata = ASMEB314LogitudinalStress(customdata)
    cfg['Result']['ASMEB314']['LogitudinalStress'] = customdata

if cfg['Default']['Analysis']['Code'] == "ASME B31.8":
    from custom.ASMEMethods import ASMEB318LogitudinalStress
    customdata = ASMEB318LogitudinalStress(customdata)
    cfg['Result']['ASMEB318']['LogitudinalStress'] = customdata

customdata = {"S": cfg['Material']['SMYS'], 
            "t" : cfg['Geometry']['DesignWT'],
            "D" : cfg['Geometry']['NominalOD'],
            "Pi": cfg['Design']['InternalPressure'],
            "Po": cfg['Design']['ExternalPressure'],
            "M": cfg['Design']['BendingMoment'],
            "Fa": cfg['Design']['AxialForce'],
            "F" : cfg['DesignFactors']['EquivalentStress'],
            "WeldFactor" : cfg['Material']['WeldFactor']['Seamless'],
            "E" : cfg['Material']['E'],
            "Poissionsratio" : cfg['Material']['Poissionsratio'],
            "T" : cfg['Result']['TemperatureDerating'],
            "Alpha" : cfg['Material']['ThermalExpansionCoefficient'],
            "T1": cfg['Design']['Temperature']['Operating'],
            "T2": cfg['Design']['Temperature']['Ambient'],
            "Condition": cfg['Design']['Condition']
}

if cfg['Default']['Analysis']['Code'] == "ASME B31.4":
    from custom.ASMEMethods import ASMEB314EquivalentStress
    customdata = ASMEB314EquivalentStress(customdata)
    cfg['Result']['ASMEB314']['EquivalentStress'] = customdata

if cfg['Default']['Analysis']['Code'] == "ASME B31.8":
    from custom.ASMEMethods import ASMEB318EquivalentStress
    customdata = ASMEB318EquivalentStress(customdata)
    cfg['Result']['ASMEB318']['EquivalentStress'] = customdata

saveDataYaml(cfg, 'results\\ASMEB31\\' + 'Summary_' + cfg['FileName'])
