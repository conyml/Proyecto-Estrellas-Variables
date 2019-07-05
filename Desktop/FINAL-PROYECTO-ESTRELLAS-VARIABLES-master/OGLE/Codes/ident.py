import pandas as pd 
import numpy as np
import glob
import os

ident=pd.DataFrame(columns=['ID_OGLE','RAJ2000.0','DECJ2000.0',
'Period_OGLE','Macho_id','Eros_id','Dasch_id'])

OGLE_ID=[]
RA=[]
DEC=[]
Period=[]
Macho=[]
Eros=[]
Dasch=[]
Survey=[]

for i in range(len(x)):
	OGLE_ID.append(x['ID_OGLE'])
	RA.append(x['RAJ2000.0'])
	DEC.append(x['DECJ2000.0'])
	Period.append(x['Period_OGLE'])
	if type(x['Macho_id'])==str:
		Macho.append(x['Macho_id'])
	else:
		Macho.append('')
	if type(x['Eros_id'])==str:
		Eros.append(x['Eros_id'])
	else:
		Eros.append('')
	if type(x['Dasch_id'])==str:
		Dasch.append(x['Dasch_id'])
	else:
		Dasch.append('')

