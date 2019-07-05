import pandas as pd 
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.gridspec as gridspec

pathV=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Old Lightcurves/V/')
pathI=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Old Lightcurves/I/')

pathO2V=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Old Lightcurves/OGLE2/V/')
pathO2I=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Old Lightcurves/OGLE2/I/')

filesV = glob.glob(os.path.join(pathV, '*.dat'))
filenamesV= [x[len(pathV):-4] for x in filesV]
filesI = glob.glob(os.path.join(pathI, '*.dat'))
filenamesI= [x[len(pathV):-4] for x in filesI]

filesO2V = glob.glob(os.path.join(pathO2V, '*.dat'))
filenamesO2V= [x[len(pathO2V):-4] for x in filesO2V]
filesO2I = glob.glob(os.path.join(pathO2I, '*.dat'))
filenamesO2I= [x[len(pathO2V):-4] for x in filesO2I]

Vepochs=[]
Vmags=[]
errorVmags=[]

for i in range(len(filenamesI)):
	if filenamesI[i] in filenamesO2I:
		algo=pd.read_csv(str(pathI+filenamesI[i])+'.dat',header=1, delimiter=',', 
		names=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band',
		'N_epoch','JD','mag','errmag'])
		algo2=pd.read_csv(str(pathO2I+filenamesI[i])+".dat",header=1, delimiter=',', 
		names=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band',
		'N_epoch','JD','mag','errmag'])
		result = algo2.append(algo)
		result.to_csv('/Users/Carolina/Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Original and Normed Magnitudes/I/'+filenamesI[i]+'.dat', sep=',', index=False)
	elif filenamesI[i] not in filenamesO2I:
		algo=pd.read_csv(str(pathI+filenamesI[i])+'.dat',header=1, delimiter=',', 
		names=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band',
		'N_epoch','JD','mag','errmag'])
		algo.to_csv(home+'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Original and Normed Magnitudes/I/'+filenamesI[i]+'.dat', sep=',', index=False)
		
for i in range(len(filenamesV)):
	try:
		if filenamesV[i] in filenamesO2V:
			algo=pd.read_csv(str(pathV+filenamesV[i])+'.dat',header=1, delimiter=',', 
			names=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band',
			'N_epoch','JD','mag','errmag'])
			algo2=pd.read_csv(str(pathO2V+filenamesV[i])+".dat",header=1, delimiter=',', 
			names=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band',
			'N_epoch','JD','mag','errmag'])
			result = algo2.append(algo)
			result.to_csv(home+'/Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Original and Normed Magnitudes/V/'+filenamesV[i]+'.dat', sep=',', index=False)
		elif filenamesV[i] not in filenamesO2V:
			algo=pd.read_csv(str(pathV+filenamesV[i])+'.dat',header=1, delimiter=',', 
			names=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band',
			'N_epoch','JD','mag','errmag'])
			algo.to_csv(home+'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Original and Normed Magnitudes/V/'+filenamesV[i]+'.dat', sep=',', index=False)
	except pd.errors.ParserError:
		pass
