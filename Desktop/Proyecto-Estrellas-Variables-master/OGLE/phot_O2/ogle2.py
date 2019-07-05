import pandas as pd 
import numpy as np
import glob
from sh import gunzip
import os
import shutil

id_star=pd.read_csv("dasch.dat",header=0, delimiter=',', 
	names=['Stars ID','Ogle2'])

cepF=pd.read_csv("cepFO4.dat", header=None, delimiter=r"\s+", 
	names=['Stars ID', 'Intensity mean I-band magnitude', 
	'Intensity mean V-band magnitude','Period', 'Uncertainty of period',
	'Time of maximum brightness (HJD-2450000)',
	'I-band amplitude (maximum-minimum)','Fourier coefficient R_21',
	'Fourier coefficient phi_21','Fourier coefficient R_31',
	'Fourier coefficient phi_31'])

lista=[x.lower() for x in id_star['Ogle2'] if 'LMC_SC' in str(x)]
print(lista)
for i in range(21):
	pathV='/Users/Carolina/Desktop/Proyecto/OGLE/phot_O2/lmc_sc'+str(i+1)+'/phot/V/'
	files= glob.glob(os.path.join(pathV, '*.dat'))
	for j in range(len(files)):
		y=files[j][46:-4].replace("/phot/V/","_")
		if y in lista:
			x=np.loadtxt(files[j]).T
			dfV=pd.DataFrame(columns=['epoch','mag','errmag'])
			dfV['epoch']=x[0]
			dfV['mag']=x[1]
			dfV['errmag']=x[2]
			dfV.to_csv('/Users/Carolina/Desktop/Proyecto/OGLE/Only_useful_O2/V/'+y+'.dat', sep=',', index=False)	

for i in range(21):
	pathI='/Users/Carolina/Desktop/Proyecto/OGLE/phot_O2/lmc_sc'+str(i+1)+'/phot/I/'
	files= glob.glob(os.path.join(pathI, '*.dat'))
	for j in range(len(files)):
		y=files[j][46:-4].replace("/phot/I/","_")
		if y in lista:
			x=np.loadtxt(files[j]).T
			dfI=pd.DataFrame(columns=['epoch','mag','errmag'])
			dfI['epoch']=x[0]
			dfI['mag']=x[1]
			dfI['errmag']=x[2]
			dfI.to_csv('/Users/Carolina/Desktop/Proyecto/OGLE/Only_useful_O2/I/'+y+'.dat', sep=',', index=False)	


