#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:59:55 2019

@author: Alvaro
"""

import os
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u

path_to_full_lc = 'full_light_curves'
file_ogle_objects = 'DASCH_Objects_list_downloaded.csv'

paths_to_full_lcs = []

for filename in os.listdir(path_to_full_lc):
    if not filename.startswith('.'):
        paths_to_full_lcs.append(os.path.join(path_to_full_lc,filename))
        
#Cargo el catálogo de estrellas de OGLE.
DASCH_OGLE_match = pd.read_csv(file_ogle_objects,
                               header = 0,
                               sep = ';',
                               usecols = ['ID','mag_I','mag_V','ra','dec'])

#leer los nombre de DASCH y coordenadas del nombre de cada archivo
ras_DASCH,decs_DASCH,IDS_DASCH = [],[], []
for DASCH_path in paths_to_full_lcs:
    DASCH_name = DASCH_path.strip().split('/')[-1].split('_')
    ra_DASCH = DASCH_name[0]
    dec_DASCH = DASCH_name[1]
    if 'APASS' in DASCH_name[2] or 'DASCH' in DASCH_name[2]:
        ID_DASCH = (DASCH_name[2]+'_'+DASCH_name[3])
    else:
        ID_DASCH = DASCH_name[2]
    ras_DASCH.append(ra_DASCH)
    decs_DASCH.append(dec_DASCH)
    IDS_DASCH.append(ID_DASCH)
    print ra_DASCH, dec_DASCH, ID_DASCH
    
#CROSSMATCH de astropy entre IDs de OGLE y DASCH por las coordenadas de cada catalogo.
DASCH_coords = SkyCoord(ras_DASCH,decs_DASCH, unit = [u.hourangle,u.deg])
OGLE_coords = SkyCoord(DASCH_OGLE_match['ra'],DASCH_OGLE_match['dec'],unit=[u.hourangle,u.deg])
idx, d2d, d3d = DASCH_coords.match_to_catalog_sky(OGLE_coords)

j = 0
DASCH_OGLE_match['DASCH ID'] = ''
for i in idx:
    DASCH_OGLE_match['DASCH ID'][i] = IDS_DASCH[j]
    j+=1
    
DASCH_OGLE_match.to_csv('DASCH-OGLE-crossmatch.csv', index = False)