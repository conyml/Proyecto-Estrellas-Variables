import pandas as pd 
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.gridspec as gridspec
from os.path import expanduser
home = expanduser("~")

pathCEPF=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables-Estrellas-Variables/OGLE Nuevo/Data/cepFO4.dat')
cepF=pd.read_csv(pathCEPF, header=None, delimiter=r"\s+", 
	names=['Stars ID', 'Intensity mean I-band magnitude', 
	'Intensity mean V-band magnitude','Period', 'Uncertainty of period',
	'Time of maximum brightness (HJD-2450000)',
	'I-band amplitude (maximum-minimum)','Fourier coefficient R_21',
	'Fourier coefficient phi_21','Fourier coefficient R_31',
	'Fourier coefficient phi_31'])

pathI_O4=os.path.join(home, 'Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Phot/phot_O4/I')
filesI_O4 = glob.glob(os.path.join(pathI_O4, '*.dat'))
filenamesI_O4= [x[len(pathI_O4):-4] for x in filesI_O4]

cepFI = cepF[cepF['Stars ID'].isin(filenamesI_O4)]
cepFI.reset_index(drop=True, inplace=True)

Iphases=[]
Imags=[]
errorImags=[]
periods=[]
names_var=[]

for i in range(len(cepFI)):
	algo=str(pathI_O4+'/'+cepFI['Stars ID'][i])
	x=np.loadtxt(algo+'.dat').T
	nn2=np.argwhere(np.isnan(np.modf((np.array(x[0])-x[0][np.argmax(x[1])])/float(cepFI['Period'][i]))[0]))
	magnitudes=list(np.delete(x[1],nn2))
	JD=np.delete(x[0],nn2)
	errormagnitudes=list(np.delete(x[2],nn2))
	phasetotal_plit=np.modf((np.array(JD)-JD[np.argmax(magnitudes)])/float(cepFI['Period'][i]))[0]
	phas1=list(np.where(phasetotal_plit>0.0, phasetotal_plit,phasetotal_plit+1.0))
	if len(phasetotal_plit)>0:
		phas2=[x+1.0 for x in phas1]
		phas=phas1+phas2
		Iphases.append(phas)
		Imags.append(magnitudes*2)
		errorImags.append(errormagnitudes*2)
		periods.append(cepFI['Period'][i])
		names_var.append(cepFI['Stars ID'][i])
		
def lightcurve(num,magband,colordot,maglist,erromag,phase_ogle,var_name,periods):
	with PdfPages(home+'/Desktop/Proyecto-Estrellas-Variables/OGLE Nuevo/Curvas/lightcurves_cepF_'+magband+'.pdf') as pdf:
		i = 0
		while i < len(maglist):
			fig=plt.figure(i)
			j = 0
			while j<num and i+j < len(maglist):
				phase=phase_ogle[j+i]
				mag=maglist[j+i]
				error=erromag[j+i]
				star=var_name[j+i]
				plit=periods[j+i]
				f=j+1
				ax= fig.add_subplot(int(num/2) ,int(num/2) ,f)
				ax.errorbar(phase,mag,yerr=error, color=colordot,fmt='o',markersize=0.8)
				#plt.scatter(phasegaia,mag,label='gaia',color=colordot,s=0.8)
				#plt.errorbar(phasegaia,mag, xerr=0.2, yerr=0.4)
				plt.xlabel('Phase', size=9)
				plt.ylabel('magnitude '+magband, size=9)
				plt.tight_layout()
				plt.axis([0,2,max(mag)+0.1,min(mag)-0.1])
				plt.title(str(star)+ ' \n'  +' \n Period: '+ str(plit), size=6)
				plt.tick_params(axis='both', which='major', labelsize=8)
				plt.tick_params(axis='both', which='minor', labelsize=8)
				j=j+1
			i=i+num
			plt.close()
			pdf.savefig(fig)
	return plt.show()

lightcurve_V=lightcurve(4,'I','red',Imags,errorImags,Iphases,names_var,periods)
