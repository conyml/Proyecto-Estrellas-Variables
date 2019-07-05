import pandas as pd 
import numpy as np
import glob
import os
from gatspy.periodic import LombScargleFast
from os.path import expanduser
home = expanduser("~")

pathO2V=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Old Lightcurves/OGLE2/V/')
pathO2I=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Old Lightcurves/OGLE2/I/')

filesO2V = glob.glob(os.path.join(pathO2V, '*.dat'))
filenamesO2V= [x[len(pathO2V):-4] for x in filesO2V]
filesO2I = glob.glob(os.path.join(pathO2I, '*.dat'))
filenamesO2I= [x[len(pathO2V):-4] for x in filesO2I]

pathV=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Original and Normed Magnitudes/All Lightcurves/V/')
pathI=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Original and Normed Magnitudes/All Lightcurves/I/')


filesV = glob.glob(os.path.join(pathV, '*.dat'))
filenamesV= [x[len(pathV):-4] for x in filesV]
filesI = glob.glob(os.path.join(pathI, '*.dat'))
filenamesI= [x[len(pathV):-4] for x in filesI]

for i in range(len(filenamesI)):
	if filenamesI[i] in filenamesO2I:
		algo=pd.read_csv(filesI[i],header=1, delimiter=',', 
		names=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey',
		'Band','N_epoch','JD','mag','errmag'])
		ls = LombScargleFast()
		ls.optimizer.period_range = (0.1,100)
		ls.fit(algo['JD'],algo['mag'])
		period = ls.best_period
		print("Best period: " + str(period) + " days")
		
		
