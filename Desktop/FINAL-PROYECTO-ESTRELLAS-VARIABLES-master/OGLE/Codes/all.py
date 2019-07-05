import pandas as pd
import os
import glob
import numpy as np


paths='/Users/Carolina/Desktop/ALL/'
files=glob.glob(os.path.join(paths, '*.dat'))

for i in range(len(files)):
	algo=pd.read_csv(files[i],
		header=0, delimiter=',', names=['HJD','MAG','BAND','SURVEY'])
	try:
		algo=algo[algo['HJD'] != 'HJD']
	except TypeError:
		continue
	#algo['HJD']=algo['HJD'].astype('float64') 
	#algo['HJD'] = np.where( algo['HJD'] > 10000.0, algo['HJD']-2450000.0, algo['HJD'])
	algo.to_csv(files[i], sep=',', index=False)


