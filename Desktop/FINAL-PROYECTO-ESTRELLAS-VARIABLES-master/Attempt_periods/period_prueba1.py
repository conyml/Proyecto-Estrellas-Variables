import pandas as pd
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

paths='/Users/Carolina/Desktop/'
files=glob.glob(os.path.join(paths, '*.dat'))

Iphases=[]
Imags=[]
periods=[]
names_var=[]

for i in range(len(files)):
	algo=pd.read_csv(files[i],
		header=0, delimiter=',', names=['HJD','MAG','ERROR','SURVEY'])
	#algo=algo2[int(len(algo2)/3):]
	nn2=np.argwhere(np.isnan(np.modf((np.array(algo['HJD'])-algo['HJD'][algo['MAG'].idxmax()])/2.8880890999999997))[0])
	magnitudes=list(np.delete(algo['MAG'],nn2))
	JD=algo['HJD'].values.tolist()
	phasetotal_plit=np.modf((np.array(JD)-JD[np.argmax(magnitudes)])/2.8880890999999997)[0]
	phas1=list(np.where(phasetotal_plit>0.0, phasetotal_plit,phasetotal_plit+1.0))
	if len(phasetotal_plit)>0:
		phas2=[x+1.0 for x in phas1]
		phas=phas1+phas2
		Iphases.append(phas)
		Imags.append(magnitudes*2)
		periods.append(2.8880890999999997)
		names_var.append('OGLE-LMC-CEP-0610')


def lightcurve(num,magband,colordot,maglist,phase_ogle,var_name,periods):
	with PdfPages('/Users/Carolina/Desktop/OGLE-LMC-CEP-0610.pdf') as pdf:
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
				plt.xlabel('Phase', size=14)
				plt.ylabel('magnitude '+magband, size=14)
				plt.axis([0,2,max(mag)+0.1,min(mag)-0.1])
				plt.title(str(star)+' DATA FROM OGLE-II'+ ' \n'  +' \n Period: '+ str(plit), size=12)
				plt.tick_params(axis='both', which='major', labelsize=10)
				plt.tick_params(axis='both', which='minor', labelsize=10)
				plt.tight_layout()
				j=j+1
			i=i+num
			plt.close()
			pdf.savefig(fig)
	return plt.show()

lightcurve_V=lightcurve(2,'I','red',Imags,Iphases,names_var,periods)
