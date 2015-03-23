
# coding: utf-8

import os as os
import numpy as np
import csv

os.system(u'wget http://www.cgd.ucar.edu/cas/catalog/surface/dai-runoff/coastal-stns-byVol-updated-oct2007.txt')




No = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(0), skiprows=1)
m2s_ratio = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(1), skiprows=1)
lonm = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(2), skiprows=1)
latm = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(3), skiprows=1)
area = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(4), skiprows=1)
Vol = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(5), skiprows=1)
nyr = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(6), skiprows=1)
yrb = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(7), skiprows=1)
yre = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(8), skiprows=1)
elev = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(9), skiprows=1)
CT = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(10),dtype=None, skiprows=1)
CN = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(11),dtype=None, skiprows=1)
River_Name = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(12),dtype=None, skiprows=1)
OCN = np.genfromtxt('coastal-stns-byVol-updated-oct2007.txt', usecols=(13),dtype=None, skiprows=1)


for i in range(len(Vol)):
    for j in range(len(Vol)-1-i):
        if Vol[j] < Vol[j+1]:
            Vol[j], Vol[j+1] = Vol[j+1], Vol[j]
            No[j], No[j+1] = No[j+1], No[j]
            m2s_ratio[j], m2s_ratio[j+1] = m2s_ratio[j+1], m2s_ratio[j]
            lonm[j], lonm[j+1] = lonm[j+1], lonm[j]
            latm[j], latm[j+1] = latm[j+1], latm[j]
            area[j], area[j+1] = area[j+1], area[j]
            nyr[j], nyr[j+1] = nyr[j+1], nyr[j]
            yrb[j], yrb[j+1] = yrb[j+1], yrb[j]
            yre[j], yre[j+1] = yre[j+1], yre[j]
            elev[j], elev[j+1] = elev[j+1], elev[j]
            CT[j], CT[j+1] = CT[j+1], CT[j]
            CN[j], CN[j+1] = CN[j+1], CN[j]
            River_Name[j], River_Name[j+1] = River_Name[j+1], River_Name[j]
            OCN[j], OCN[j+1] = OCN[j+1], OCN[j]
            



col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []
col10 = []
col11 = []
col12 = []
col13 = []
col14 = []
col1.append('No')
col2.append('m2s_ratio')
col3.append('lonm')
col4.append('latm')
col5.append('area')
col6.append('Vol')
col7.append('nyr')
col8.append('yrb')
col9.append('yre')
col10.append('elev')
col11.append('CT')
col12.append('CN')
col13.append('River_Name')
col14.append('OCN')
for i in range(300):
    col1.append(No[i])
    col2.append(m2s_ratio[i])
    col3.append(lonm[i])
    col4.append(latm[i])
    col5.append(area[i])
    col6.append(Vol[i])
    col7.append(nyr[i])
    col8.append(yrb[i])
    col9.append(yre[i])
    col10.append(elev[i])
    col11.append(CT[i])
    col12.append(CN[i])
    col13.append(River_Name[i])
    col14.append(OCN[i])





rows = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14)
with open("top_300_rios.csv", "w") as output:
    for row in rows:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(row)




