import pandas as pd 
import numpy as np
import glob
import os
from os.path import expanduser
home = expanduser("~")

pathV=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Original and Normed Magnitudes/All Lightcurves/V/')
pathI=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Original and Normed Magnitudes/All Lightcurves/I/')

filesV = glob.glob(os.path.join(pathV, '*.dat'))
filenamesV= [x[len(pathV):-4] for x in filesV]
filesI = glob.glob(os.path.join(pathI, '*.dat'))
filenamesI= [x[len(pathV):-4] for x in filesI]
amplitude=0.691

def normed(mi,ma,amp):
	algo=[]
	for i in range(5000):
		algo.append((ma-mi)*i*0.001)
	return min(algo, key=lambda x:abs(x-amp))
		
for i in range(len(filesV)):
	algo=pd.read_csv(filesV[i],header=1, delimiter=',',
	names=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band',
	'N_epoch','JD','mag','errmag'])
	try:
		valor=normed(min(algo['mag']),max(algo['mag']),amplitude)
		x=valor*algo['mag']
		df=pd.DataFrame(columns=['Normed_Mag','Band','Survey'])
		df['Normed_Mag']=x
		df['Band']=algo['Band']
		df['Survey']=algo['Survey']
		df.to_csv(home+'/Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Original and Normed Magnitudes/Normed Magnitudes/V/'+filenamesV[i]+'.dat', sep=',', index=False)		
	except ValueError:
		pass
	
for i in range(len(filesI)):
	algo=pd.read_csv(filesI[i],header=1, delimiter=',',
	names=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band',
	'N_epoch','JD','mag','errmag'])
	try:
		valor=normed(min(algo['mag']),max(algo['mag']),amplitude)
		x=valor*algo['mag']
		df=pd.DataFrame(columns=['Normed_Mag','Band','Survey'])
		df['Normed_Mag']=x
		df['Band']=algo['Band']
		df['Survey']=algo['Survey']
		df.to_csv(home+'/Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Original and Normed Magnitudes/Normed Magnitudes/I/'+filenamesI[i]+'.dat', sep=',', index=False)		
	except ValueError:
		pass
			
	
	


