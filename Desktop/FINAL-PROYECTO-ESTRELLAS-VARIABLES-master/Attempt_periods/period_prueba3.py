import pandas as pd
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

paths='/Users/Carolina/Desktop/'
files=glob.glob(os.path.join(paths, '*.dat'))

algo=pd.read_csv(files[0],
	header=0, delimiter=',', names=['HJD','MAG','BAND','SURVEY'])

import astropy.units as u
from astropy.stats import BoxLeastSquares
algo['HJD'] = np.where( algo['HJD'] > 10000.0, algo['HJD']+2450000.0, algo['HJD'])
t=algo['HJD'].values.tolist()
y = algo['MAG'].values.tolist()

model = BoxLeastSquares(t * u.day, y, dy=0.01)            
periods = np.linspace(8.8, 8.9, 1000) * u.day
periodogram = model.power(periods, 0.2)
plt.plot(periodogram.period, periodogram.power)
print(periodogram.period[np.argmax(periodogram.power)])
plt.axis([12,20,0,5e3])
plt.show()

Iphases=[]
Imags=[]
periods=[]
names_var=[]

for i in range(len(files)):
	algo2=pd.read_csv(files[i],
		header=0, delimiter=',', names=['HJD','MAG','BAND','SURVEY'])
	algo2['HJD'] = np.where( algo['HJD'] < 10000.0, algo['HJD']+2450000.0, algo['HJD'])
	algo2['HJD']=algo2['HJD'].astype('float64') 
	algo3 = algo2.drop(algo2[algo2['HJD']<=2430000.0].index)
	algo = algo3.drop(algo3[algo3['HJD']>=2431000.0].index)
	nn2=np.argwhere(np.isnan(np.modf((np.array(algo['HJD'])-algo['HJD'][np.argmax(algo['MAG'])])/7.1807603))[0])
	magnitudes=list(np.delete(algo['MAG'],nn2))
	algo['HJD']=np.delete(algo['HJD'],nn2)
	JD=algo['HJD'].values.tolist()
	phasetotal_plit=np.modf((np.array(JD)-JD[np.argmax(magnitudes)])/7.1807603)[0]
	phas1=list(np.where(phasetotal_plit>0.0, phasetotal_plit,phasetotal_plit+1.0))
	if len(phasetotal_plit)>0:
		phas2=[x+1.0 for x in phas1]
		phas=phas1+phas2
		Iphases.append(phas)
		Imags.append(magnitudes*2)
		periods.append(7.1807603)
		names_var.append('OGLE-LMC-CEP-0033')

def lightcurve(num,magband,colordot,maglist,phase_ogle,var_name,periods):
	with PdfPages('/Users/Carolina/Desktop/OGLE-LMC-CEP-0033.pdf') as pdf:
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
				plt.axis([0,2,max(mag)+0.1,min(mag)-0.1])
				plt.title(' \n' + str(names_var)+ ' \n'  +' \n Period: '+ str(plit), size=6)
				plt.tick_params(axis='both', which='major', labelsize=8)
				plt.tick_params(axis='both', which='minor', labelsize=8)
				plt.tight_layout()
				j=j+1
			i=i+num
			plt.close()
			pdf.savefig(fig)
	return plt.show()

lightcurve_V=lightcurve(4,'I','red',Imags,Iphases,names_var,periods)
