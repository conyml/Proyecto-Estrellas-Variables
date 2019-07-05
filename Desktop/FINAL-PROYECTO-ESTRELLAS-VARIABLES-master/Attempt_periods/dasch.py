import pandas as pd
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

paths='/Users/Carolina/Desktop/light_curves/'
files=glob.glob(os.path.join(paths, '*.dat'))
filenames=[x[len(paths):-4] for x in files]

files=sorted(files)

ident=pd.read_csv('ident.txt',
	header=0, delimiter=',', names=['ID_OGLE','RAJ2000.0','DECJ2000.0',
	'N_epoch_OGLE','ID_DASCH','N_epoch_DASCH','ID_EROS','N_epoch_EROS',
	'ID_MACHO','N_epoch_Macho','N_total','OGLE_Period'])

ident = ident.drop(ident[ident['N_epoch_DASCH']==0.0].index)
ident.reset_index(drop=True, inplace=True)

ident=ident.sort_values(by=['ID_OGLE'])

#names=ident['ID_OGLE'].values.tolist()
#algo2=[x for x in filenames if x in names]
#print(len(algo2))

#import astropy.units as u
#from astropy.stats import BoxLeastSquares
#algo['HJD'] = np.where( algo['HJD'] < 10000.0, algo['HJD']+2450000.0, algo['HJD'])
#t=algo['HJD'].values.tolist()
#y = algo['MAG'].values.tolist()

#model = BoxLeastSquares(t * u.day, y, dy=0.01)            
#periods = np.linspace(7.1, 7.2, 1000) * u.day
#periodogram = model.power(periods, 0.2)
#plt.plot(periodogram.period, periodogram.power)
#print(periodogram.period[np.argmax(periodogram.power)])
#plt.axis([12,20,0,5e3])
#plt.show()

Iphases=[]
Imags=[]
periods=[]
names_var=[]
epochs=[]

for i in range(len(ident)):
	#algo=pd.read_csv(paths+ident['ID_OGLE'][i]+'.dat',
		#header=0, delimiter=',', names=['HJD','MAG','BAND','SURVEY'])
	#algo['HJD'] = np.where( algo['HJD'] < 10000.0, algo['HJD']+2450000.0, algo['HJD'])
	algo2=pd.read_csv(paths+ident['ID_OGLE'][i]+'.dat',
		header=0, delimiter=',', names=['HJD','MAG','BAND','SURVEY'])
	algo2['HJD'] = np.where( algo2['HJD'] < 10000.0, algo2['HJD']+2450000.0, algo2['HJD'])
	algo2['HJD']=algo2['HJD'].astype('float64') 
	algo3 = algo2.drop(algo2[algo2['HJD']<=2430000.0].index)
	algo = algo3.drop(algo3[algo3['HJD']>=2431000.0].index)
	nn2=np.argwhere(np.isnan(np.modf((np.array(algo['HJD'])-algo['HJD'][np.argmax(algo['MAG'])])/ident['OGLE_Period'][i]))[0])
	magnitudes=list(np.delete(algo['MAG'],nn2))
	algo['HJD']=np.delete(algo['HJD'],nn2)
	JD=algo['HJD'].values.tolist()
	phasetotal_plit=np.modf((np.array(JD)-JD[np.argmax(magnitudes)])/ident['OGLE_Period'][i])[0]
	phas1=list(np.where(phasetotal_plit>0.0, phasetotal_plit,phasetotal_plit+1.0))
	if len(phasetotal_plit)>0:
		epochs.append(JD*2)
		phas2=[x+1.0 for x in phas1]
		phas=phas1+phas2
		Iphases.append(phas)
		Imags.append(magnitudes*2)
		periods.append(ident['OGLE_Period'][i])
		names_var.append(ident['ID_OGLE'][i])

def lightcurve(name,num,magband,colordot,maglist,phase_ogle,var_name,periods):
	with PdfPages('/Users/Carolina/Desktop/Lightcurves_Dasch_'+name+'.pdf') as pdf:
		i = 0
		while i < len(maglist):
			fig=plt.figure(i)
			j = 0
			while j<num and i+j < len(maglist):
				phase=phase_ogle[j+i]
				mag=maglist[j+i]
				star=var_name[j+i]
				plit=periods[j+i]
				f=j+1
				ax= fig.add_subplot(int(num/2) ,int(num/2) ,f)
				plt.scatter(phase,mag,label='gaia',color=colordot,s=0.8)
				plt.xlabel('Phase', size=9)
				plt.ylabel('magnitude '+magband, size=9)
				plt.tight_layout()
				plt.axis([0,2,max(mag)+0.1,min(mag)-0.1])
				plt.title(' \n' + str(star)+ ' \n'  +' \n Period: '+ str(plit), size=6)
				plt.tick_params(axis='both', which='major', labelsize=6)
				plt.tick_params(axis='both', which='minor', labelsize=6)
				plt.xticks(rotation=90)
				j=j+1
			i=i+num
			plt.close()
			pdf.savefig(fig)
	return plt.show()

#lightcurve_V=lightcurve('All_Epoch',4,'I','red',Imags,Iphases,names_var,periods)
lightcurve_all=lightcurve('Not_All_Epoch_31',4,'B','red',Imags,Iphases,names_var,periods)
