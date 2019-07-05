#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:20:06 2019

@author: Alvaro
"""

import os
import pandas as pd
import re
import numpy as np

path_to_full_LC = 'full_light_curves'
catalog_file = 'DASCH-OGLE-crossmatch.csv'

paths_to_full_LCs = []
for filename in os.listdir(path_to_full_LC):
    paths_to_full_LCs.append(os.path.join(path_to_full_LC, filename))
    
df = pd.read_csv(paths_to_full_LCs[0],
                 header = 0,
                 skiprows = [0,2],
                 sep = '\t')

catalog = pd.read_csv(catalog_file)

norm_amplitude = 0.691

for name in paths_to_full_LCs:
    df = pd.read_csv(name,
                 header = 0,
                 skiprows = [0,2],
                 sep = '\t',
                 usecols = ['Date','magcal_local'])
    df['Band'] = 'B'
    df['Survey'] = 'DASCH'
    df.rename(columns={'Date':'HJD', 'magcal_local':'mag'}, inplace= True)
    df = df.reindex(columns=['HJD','mag', 'Band', 'Survey'])
    
    #Find amplitude eliminating the outliers
    mag = df.copy()
    mag.drop(mag[(np.median(mag['mag']) - 1.5 > mag['mag']) | (np.median(mag['mag']) + 1.5 < mag['mag'])].index, inplace = True)
    amplitude = max(mag['mag'])-min(mag['mag'])
    
    #normalice the magnitude to CEP_0012 OGLE.
    df['mag'] = df['mag'].apply(lambda x: x*norm_amplitude/amplitude)
    
    filename = name.split('/')[1][:-4]
    DASCH_ID = re.split('(?<=\d)[_](?!\s)',filename)[-2]
    OGLE_ID = catalog.loc[catalog['DASCH ID'] == DASCH_ID]
    OGLE_ID = OGLE_ID.iloc[0]['ID']
    df.to_csv('light_curves_normed/'+OGLE_ID+'.dat',index=False)
    print OGLE_ID
    