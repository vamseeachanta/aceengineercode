# -*- coding: utf-8 -*-
"""
Created on September 16 2018
"""
'''
Author: Vamsee Achanta
Date Updated: 2018-09-20
Objective: To generate catenary riser shape and evaluate static configuration
Run instructions with:
 Default yml file : python APISTD2RD.py
 Update default yml with parameters in 12.yml: python APISTD2RD.py 12.yml
 Outputs: DataFrame with outputs
'''
import math
from math import *

import matplotlib.pyplot as plt
import numpy as np
# from catenarycalculation import *
from dataManager.loadConfiguration import loadConfiguration
from scipy.interpolate import spline

configParams = loadConfiguration('dataManager//catenary.ini')

def catenaryEquation(catenary):
    
    ##catenary equation.
    #Cross Sectional Area of the Thread.
    catenaryA=(((catenary.diameter/2)**2)*math.pi)
    print("catenaryArea : ","{:.2f}".format(catenaryA))
    
    #Unit Weight of the mooring Line in water
    catenaryW=catenary.specificGravity*catenaryA
    print("catenaryWaterdepth : ","{:.2f}".format(catenaryW))

    #Length of the suspended Mooring Line.
    catenaryS=(sqrt(catenary.distance*(2*catenary.force/catenaryW-catenary.distance)))
    print("catenarySuspendedMooringLine : ","{:.2f}".format(catenaryS))

    #Horizontal Distance.
    catenaryX=(((catenary.force/catenaryW)-catenary.distance)*log((catenaryS+(catenary.force/catenaryW))/((catenary.force/catenaryW)-catenary.distance)))
    print("catenaryHorizontalDistance : ","{:.2f}".format(catenaryX))

    #weight of the suspended chain
    catenaryV=(catenaryW*catenaryS)
    print("catenarysuspendedchain : ","{:.2f}".format(catenaryV))

    #normalized horizontal tension component
    catenaryT_0= (catenary.force*catenaryX/sqrt(catenaryS**2+catenaryX**2))
    print("catenaryhorizontaltensioncomponent : ","{:.2f}".format(catenaryT_0))

    #catenary shape parameter
    catenaryb=(catenary.specificGravity*9.81*catenaryA/catenaryT_0)
    print("catenaryshapeparameter : ","{:.2f}".format(catenaryb))
    
    #calculating the horX values
    node = range(11)
    factor = []
    horX = []
    for i in node:
        f = i/10
        factor.append(f)
        h = catenaryX*f
        horX.append(h)
    print(factor)
    print(horX)
    factor2 = []
    #calculating the shape of a catenary mooring line noted as f2
    for j in factor:
        f2 = (-1/catenaryb)*(math.log(cos(catenaryb*j)))
        factor2.append(f2)
    print(factor2)
    print(factor[10])
    verY= []
    #calculating the verY values
    for j in factor2:
        y = (j*catenary.distance)/factor2[10]
        verY.append(y)
    print(verY)

    #Plot the graph in smooth line.
    x=np.array(horX) 
    y=np.array(verY)
    x_smooth = np.linspace(x.min(),x.max(),300)
    y_smooth = spline(x,y, x_smooth)
    
    plt.plot(x_smooth,y_smooth)
    #it creates plot X-axis name, fontsize and colour
    plt.xlabel('Horizontal distance[m]', fontsize=12, fontweight='bold', color='black')
    #it creates plot Y-axis name, fontsize and colour 
    plt.ylabel('Distance from seabed [m]', fontsize=12, fontweight='bold', color='black')
    #it creates plot tittle, color and size
    plt.title('Catenary Mooring Line Shape',fontsize=14, fontweight='bold', color='black')
    plt.savefig("Horizontal distance[m] vs Distance from seabed [m].png",dpi=800)
    plt.show()

catenaryEquation(configParams.catenary)
