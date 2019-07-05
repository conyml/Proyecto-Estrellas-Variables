import pandas as pd 
import numpy as np
import glob
import os
from os.path import expanduser
home = expanduser("~")

pathIDENT=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Data/ident.dat')
id_star=pd.read_csv(pathIDENT,header=None, delimiter=r"\s+", 
	names=['Stars ID','Mode(s) of pulsation','Right ascension J2000.0',
	'Declination J2000.0',
	'OGLE-IV ID', 'OGLE-III ID','OGLE-II ID','Other designation (from GCVS)'])


ident = id_star.drop(id_star[id_star['Mode(s) of pulsation']!='F'].index)

pathV_O4=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Phot/phot_O4/V')
pathI_O4=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Phot/phot_O4/I')

pathV_O3=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Phot/phot_O3/V')
pathI_O3=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Phot/phot_O3/I')

filesV_O4 = glob.glob(os.path.join(pathV_O4, '*.dat'))
filenamesV_O4= [x[len(pathV_O4):-4] for x in filesV_O4]
filesI_O4 = glob.glob(os.path.join(pathI_O4, '*.dat'))
filenamesI_O4= [x[len(pathV_O4):-4] for x in filesI_O4]

filesV_O3 = glob.glob(os.path.join(pathV_O3, '*.dat'))
filenamesV_O3= [x[len(pathV_O4):-4] for x in filesV_O3]
filesI_O3 = glob.glob(os.path.join(pathI_O3, '*.dat'))
filenamesI_O3= [x[len(pathV_O4):-4] for x in filesI_O3]

identV = ident[ident['Stars ID'].isin(filenamesV_O4)]
identV.reset_index(drop=True, inplace=True)

identI = ident[ident['Stars ID'].isin(filenamesI_O4)]
identI.reset_index(drop=True, inplace=True)


Vepochs=[]
Vmags=[]
errorVmags=[]
surveyV=[]

for i in range(len(identV)):
	if identV['Stars ID'][i] in filenamesV_O3:
		algo=str(pathV_O3+'/'+identV['Stars ID'][i])
		algo2=str(pathV_O4+'/'+identV['Stars ID'][i])
		x=np.loadtxt(algo+'.dat').T
		y=np.loadtxt(algo2+'.dat').T
		Vepochs.append(list(x[0])+list(y[0]))
		Vmags.append(list(x[1])+list(y[1]))
		errorVmags.append(list(x[2])+list(y[2]))
	if identV['Stars ID'][i] not in filenamesV_O3:
		y=np.loadtxt(algo2+'.dat').T
		Vepochs.append(list(y[0]))
		Vmags.append(list(y[1]))
		errorVmags.append(list(y[2]))
		surveyV.append('OGLE4')


Iepochs=[]
Imags=[]
errorImags=[]
surveyI=[]

for i in range(len(identI)):
	if identI['Stars ID'][i] in filenamesI_O3:
		algo=str(pathI_O3+'/'+identI['Stars ID'][i])
		algo2=str(pathI_O4+'/'+identI['Stars ID'][i])
		x=np.loadtxt(algo+'.dat').T
		y=np.loadtxt(algo2+'.dat').T
		Iepochs.append(list(x[0])+list(y[0]))
		Imags.append(list(x[1])+list(y[1]))
		errorImags.append(list(x[2])+list(y[2]))
		if len(list(y[1]))!=0:
			surveyI.append('OGLE3/OGLE4')
	if identI['Stars ID'][i] not in filenamesI_O3:
		y=np.loadtxt(algo2+'.dat').T
		Iepochs.append(list(y[0]))
		Imags.append(list(y[1]))
		errorImags.append(list(y[2]))
		surveyI.append('OGLE4')
		
for i in identV.index:
	dfV=pd.DataFrame(columns=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band','N_epoch','JD','mag','errmag'])
	dfV['JD']=Vepochs[i]
	dfV['mag']=Vmags[i]
	dfV['errmag']=errorVmags[i]
	dfV['Survey']=surveyV[i]
	dfV['ID_OGLE']=str(identV['Stars ID'][i])
	dfV['RAJ2000.0']=identV['Right ascension J2000.0'][i]
	dfV['DECJ2000.0']=identV['Declination J2000.0'][i]
	dfV['Band']=str('V')
	dfV['N_epoch']=len(Vmags[i])
	dfV.to_csv(home+'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Lightcurves OGLE/V/'+identV['Stars ID'][i]+'.dat', sep=',', index=False)		

for i in identI.index:	
	dfI=pd.DataFrame(columns=['ID_OGLE','RAJ2000.0','DECJ2000.0','Survey','Band','N_epoch','JD','mag','errmag'])
	dfI['JD']=Iepochs[i]
	dfI['mag']=Imags[i]
	dfI['errmag']=errorImags[i]
	dfI['Survey']=surveyI[i]
	dfI['ID_OGLE']=str(identI['Stars ID'][i])
	dfI['RAJ2000.0']=identI['Right ascension J2000.0'][i]
	dfI['DECJ2000.0']=identI['Declination J2000.0'][i]
	dfI['Band']=str('I')
	dfI['N_epoch']=len(Imags[i])
	dfI.to_csv(home+'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Lightcurves OGLE/I/'+identI['Stars ID'][i]+'.dat', sep=',', index=False)	
