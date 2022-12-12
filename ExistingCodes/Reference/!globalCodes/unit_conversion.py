# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 09:01:48 2017

@author: liqi1
"""
from cmath import pi


class unit_conversion(object):
    '''
    Description: self here = unit
    '''
    def __init__(self):
        # meter & foot
        self.m2ft = 1000.0/(12.0*25.4)
        self.ft2m = 1.0/self.m2ft
        # meter & inch
        self.in2m = 25.4/1000.0
        self.m2in = 1.0/self.in2m
        # rpm & radians per second
        self.rpm2radps = 2.0*pi/60.0
        self.radps2rpm = 1.0/self.rpm2radps
        # feet per hour & meter per second
        self.ftph2mps = 0.000084667
        self.mps2ftph = 1.0/self.ftph2mps
        # Newton & pound force
        self.n2klb = 0.000224809
        self.klb2n = 1.0/self.n2klb
        self.n2lb = self.n2klb*1000.0
        self.lb2n = 1.0/self.n2lb
        # Newton meter & pound feet
        self.nm2lbft = 0.737562121
        self.lbft2nm = 1.0/self.nm2lbft
        # Gallon & cubic meter
        self.gal2m3 = 0.003785412
        self.m32gal = 1.0/self.gal2m3
        # Gallon per minutes & cubic meter per second
        self.galpm2m3ps = self.gal2m3/60.0
        self.m3ps2galpm = 1.0/self.galpm2m3ps
        # pound per gallon & Kilogram per cubic meter
        self.lbpgal2kgpm3 = 119.826427317
        self.kgpm32lbpgal = 1.0/self.lbpgal2kgpm3
        # radians & degrees
        self.rad2deg = 180.0/pi
        self.deg2rad = 1.0/self.rad2deg
        # psi & Pascal
        self.psi2pa = 6894.757293178
        self.pa2psi = 1.0/self.psi2pa
        # pound & Kilogram
        self.lb2kg = 0.45359237
        self.kg2lb = 1.0/self.lb2kg
        # rpm & rps
        self.rpm2rps = 1/60
        self.rps2rpm = 1.0/self.rpm2rps
        
def unit_convert_to_si(imp, unit):
    si = imp*unit
    return si

def unit_convert_to_imp(si, unit):
    imp = si*unit
    return imp

def convert_RPM_to_omega(RPM):
    omega = 2.0*pi/60.0*RPM
    return omega
    
def convert_omega_to_RPM(omegaRPM):
    RPM = 60.0*omegaRPM/(2.0*pi)
    return RPM