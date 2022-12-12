# -*- coding: utf-8 -*-
"""
Created on September 21 2018
"""
'''
Author: Vamsee Achanta
Date Updated: 2018-09-21
Objective: To generate pipe properties
'''
import math


def pipeProperties(cfg, FluidDensity, Buoyancy = False):
    cfg = steelSectionProperties(cfg)
    cfg = insulationSectionProperties(cfg)
    if Buoyancy == True:
        cfg = buoyancySectionProperties(cfg)
    else:
        cfg['BuoyancySection'] = None
    cfg = equivalentPipe(cfg, FluidDensity, Buoyancy)

    return(cfg)

def steelSectionProperties(cfg):
    OD = cfg["geometry"]["NominalOD"]
    ID = cfg["geometry"]["NominalID"]
    data = {"OD": OD, "ID": ID}
    cfg['SteelSection'] = sectionProperties(data)

    return cfg

def insulationSectionProperties(cfg):
    OD = cfg["geometry"]["NominalOD"]+2*cfg["geometry"]["ExternalCoating"]['Thickness']
    ID = cfg["geometry"]["NominalOD"]
    data = {"OD": OD, "ID": ID}
    cfg['InsulationSection'] = sectionProperties(data)

    return cfg

def buoyancySectionProperties(cfg):
    OD = cfg['InsulationSection']["OD"]+2*cfg["LazyWaveCatenaryDefinition"]["UniformBuoyancy"]['Thickness']
    ID = cfg['InsulationSection']["OD"]
    data = {"OD": OD, "ID": ID}
    cfg['BuoyancySection'] = sectionProperties(data)

    return cfg

def sectionProperties(data):

    A  = (math.pi/4)*(data['OD']**2-data['ID']**2)
    Ai = (math.pi/4)*(data['ID']**2)
    Ao = (math.pi/4)*(data['OD']**2)
    I = (math.pi/64)*(data['OD']**4-data['ID']**4)

    data.update({"A": A, "Ai": Ai, "Ao": Ao, "I": I})

    return data

def equivalentPipe(cfg, FluidDensity, Buoyancy = False):
    if (cfg['geometry']['Strakes']['BaseThickness'] == None and Buoyancy == False):
        massPerUnitLength = cfg['SteelSection']['A']*cfg['Material']['Steel']['Rho']*(0.0254**2) \
                        + cfg['InsulationSection']['A']*cfg['Material']['ExternalCoating']['Rho']*(0.0254**2) \
                        + cfg['SteelSection']['Ai']*FluidDensity*(0.0254**2)

        weightPerUnitLength = (cfg['SteelSection']['A']*cfg['Material']['Steel']['Rho']*(0.0254**2)  \
                        + cfg['InsulationSection']['A']*cfg['Material']['ExternalCoating']['Rho']*(0.0254**2) \
                        + cfg['SteelSection']['Ai']*FluidDensity*(0.0254**2)     \
                        - cfg['InsulationSection']['Ao']*cfg['Material']['SeaWater']['Rho']*(0.0254**2) \
                        )*cfg['default']['Constants']['g']
    elif(cfg['geometry']['Strakes']['BaseThickness'] != None and Buoyancy == False):
        massPerUnitLength = cfg['SteelSection']['A']*cfg['Material']['Steel']['Rho']*(0.0254**2) \
                        + cfg['InsulationSection']['A']*cfg['Material']['ExternalCoating']['Rho']*(0.0254**2) \
                        + cfg['Material']['Strakes']['MassPerUnitLength']                           \
                        + cfg['SteelSection']['Ai']*FluidDensity*(0.0254**2)

        weightPerUnitLength = (cfg['SteelSection']['A']*cfg['Material']['Steel']['Rho']*(0.0254**2)  \
                        + cfg['InsulationSection']['A']*cfg['Material']['ExternalCoating']['Rho']*(0.0254**2) \
                        + cfg['SteelSection']['Ai']*FluidDensity*(0.0254**2)     \
                        - cfg['InsulationSection']['Ao']*cfg['Material']['SeaWater']['Rho']*(0.0254**2) \
                        )*cfg['default']['Constants']['g']                                  \
                        + cfg['Material']['Strakes']['WeightPerUnitLength']   
    elif(Buoyancy == True):
        massPerUnitLength = cfg['SteelSection']['A']*cfg['Material']['Steel']['Rho']*(0.0254**2) \
                        + cfg['InsulationSection']['A']*cfg['Material']['ExternalCoating']['Rho']*(0.0254**2) \
                        + cfg['BuoyancySection']['A']*cfg['Material']['Buoyancy']['Rho']*(0.0254**2) \
                        + cfg['SteelSection']['Ai']*FluidDensity*(0.0254**2)

        weightPerUnitLength = (cfg['SteelSection']['A']*cfg['Material']['Steel']['Rho']*(0.0254**2)  \
                        + cfg['InsulationSection']['A']*cfg['Material']['ExternalCoating']['Rho']*(0.0254**2) \
                        + cfg['BuoyancySection']['A']*cfg['Material']['Buoyancy']['Rho']*(0.0254**2) \
                        + cfg['SteelSection']['Ai']*FluidDensity*(0.0254**2)     \
                        - cfg['BuoyancySection']['Ao']*cfg['Material']['SeaWater']['Rho']*(0.0254**2) \
                        )*cfg['default']['Constants']['g']                                  \

    cfg['equivalentPipe'] = {"weightPerUnitLength": weightPerUnitLength, 'massPerUnitLength': massPerUnitLength}

    return(cfg)

def buoyancyFactorAndDiameter():
    pass
