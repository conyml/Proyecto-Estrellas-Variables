import pandas as pd 
import numpy as np
import glob
import os

id_star=pd.read_csv("/Users/Carolina/Desktop/Proyecto/OGLE/ident.dat",header=None, delimiter=r"\s+", 
	names=['Stars ID','Mode(s) of pulsation','Right ascension J2000.0',
	'Declination J2000.0','OGLE-IV ID', 'OGLE-III ID',
	'OGLE-II ID','Other designation (from GCVS)'])

ident = id_star.drop(id_star[id_star['Mode(s) of pulsation']!='F'].index)

#la idea era hacer un pd.contain pero no funciono porque habian nan y no los reconocia como str
lista=[[x.lower(),y,z,w] for x,y,z,w in zip(ident['OGLE-II ID'],
ident['Stars ID'],ident['Right ascension J2000.0'],ident['Declination J2000.0']) if 'LMC_SC' in str(x)]

O2=[x[0] for x in lista]
O4=[x[1] for x in lista]
RA=[x[2] for x in lista]
DEC=[x[3] for x in lista]

for i in range(21):
	pathV='/Users/Carolina/Desktop/Proyecto/OGLE/phot_O2/lmc_sc'+str(i+1)+'/phot/V/'
	files= glob.glob(os.path.join(pathV, '*.dat'))
	for j in range(len(files)):
		y=files[j][46:-4].replace("/phot/V/","_")
		if y in O2:
			try:
				x=np.loadtxt(files[j]).T
				if x[0].size>1:
					try:
						dfV=pd.DataFrame(columns=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band','N_epoch','HJD','mag','errmag'])
						dfV['HJD']=[round(x-2450000.0,8) for x in x[0]]
						dfV['mag']=x[1]
						dfV['errmag']=x[2]
						dfV['ID_OGLE']=str(O4[O2.index(y)])
						dfV['RAJ2000.0']=str(RA[O2.index(y)])
						dfV['DECJ2000.0']=str(DEC[O2.index(y)])
						dfV['Band']=str('V')
						dfV['Survey']='OGLE2'
						if type(x[0])!=np.float64:
							dfV['N_epoch']=len(x[0])
						dfV.to_csv('/Users/Carolina/Desktop/Proyecto/OGLE/Lightcurves OGLE/OGLE2/V/'+O4[O2.index(y)]+'.dat', sep=',', index=False)
					except IndexError:
						pass	
			except IndexError:
				pass
				
for i in range(21):
	pathI='/Users/Carolina/Desktop/Proyecto/OGLE/phot_O2/lmc_sc'+str(i+1)+'/phot/I/'
	files= glob.glob(os.path.join(pathI, '*.dat'))
	for j in range(len(files)):
		y=files[j][46:-4].replace("/phot/I/","_")
		if y in O2:
			try:
				x=np.loadtxt(files[j]).T
				if x[0].size>1:
					try:
						dfI=pd.DataFrame(columns=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band','N_epoch','HJD','mag','errmag'])
						dfI['HJD']=[round(x-2450000.0,8) for x in x[0]]
						dfI['mag']=x[1]
						dfI['errmag']=x[2]
						dfI['ID_OGLE']=str(O4[O2.index(y)])
						dfI['RAJ2000.0']=str(RA[O2.index(y)])
						dfI['DECJ2000.0']=str(DEC[O2.index(y)])
						dfI['Band']=str('I')
						dfV['Survey']='OGLE2'
						if type(x[0])!=np.float64:
							dfI['N_epoch']=len(x[0])
						dfI.to_csv('/Users/Carolina/Desktop/Proyecto/OGLE/Lightcurves OGLE/OGLE2/I/'+O4[O2.index(y)]+'.dat', sep=',', index=False)
					except IndexError:
						pass	
			except IndexError:
				pass
