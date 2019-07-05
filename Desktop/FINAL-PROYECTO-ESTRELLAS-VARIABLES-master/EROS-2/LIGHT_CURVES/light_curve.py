#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:37:31 2019

@author: constanzamunoz
"""

""""
Lee curvas de luz de EROS en base a archivo eros_id.time (que tiene asociado 
un ogle_id) y grafica la curva en banda B y R.
""""

import numpy as np
import matplotlib.pyplot as plt

eros_id = 'lm0627m14174'
ogle_id = 'OGLE-LMC-CEP-3352 ' 

file_in = np.loadtxt(object+'.time')
date = file_in[:,0]    
MagR = file_in[:,1]  
ErMagR = file_in[:,2]
MagB = file_in[:,3]  
ErMagB = file_in[:,4]

date_modified_B = np.array([])
MagB_modified = np.array([])
ErMagB_modified = np.array([])
c_B = 0
for i in MagB:
    if i != 99.999:
        MagB_modified = np.append(MagB_modified, i)
        date_modified_B = np.append(date_modified_B, date[c_B])
        ErMagB_modified = np.append(ErMagB_modified, ErMagB[c_B])
    else:
        pass
    c_B = c_B + 1   

date_modified_R = np.array([])
MagR_modified = np.array([])
ErMagR_modified = np.array([])
c_R = 0
for i in MagR:
    if i != 99.999:
        MagR_modified = np.append(MagR_modified, i)
        date_modified_R = np.append(date_modified_R, date[c_R])
        ErMagR_modified = np.append(ErMagR_modified, ErMagR[c_R])
    else:
        pass
    c_R = c_R + 1   
    

    
    
fig = plt.figure(figsize=(8,5))
plt.errorbar(date_modified_B, MagB_modified, yerr=ErMagB_modified, fmt='o',
             color = 'blue')
plt.gca().invert_yaxis()
plt.title("EROS ID: "+eros_id+ "    OGLE ID: " +ogle_id)
plt.xlabel("Time [days] (HJD - 2450000)")
plt.ylabel("Mag B")
plt.show()

fig = plt.figure(figsize=(8,5))

plt.errorbar(date_modified_R, MagR_modified, yerr=ErMagR_modified, fmt='o', 
             color= 'red')
plt.gca().invert_yaxis()
plt.title("EROS ID: "+eros_id+"     OGLE ID: " +ogle_id)
plt.xlabel("Time [days] (HJD - 2450000)")
plt.ylabel("Mag R")
plt.show()

"""
IGNORAR ESTO:
buscar en ogle y hacer crossmatch con los objetos que tengo, y de ahi extraer 
fotometría.
http://ogle.astrouw.edu.pl
ident.dat contiene las coordenadas 
cepF.dat contienen los periodos en modo fundamental
"""