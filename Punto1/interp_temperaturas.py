
# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate



df = pd.read_csv('Calentamientoglobal.csv')




bog = df[df.ciudad == "Bogota"]
cal = df[df.ciudad == "Cali"]
buc = df[df.ciudad == "Bucaramanga"]
bar = df[df.ciudad == "Barranquilla"]
ipi = df[df.ciudad == "Ipiales"]


del bog['anio']
del bog['mes']
del bog['ciudad']
del cal['anio']
del cal['mes']
del cal['ciudad']
del buc['anio']
del buc['mes']
del buc['ciudad']
del bar['anio']
del bar['mes']
del bar['ciudad']
del ipi['anio']
del ipi['mes']
del ipi['ciudad']

bogts = bog['fecha'].tolist()
bogtsint = np.linspace(0,len(bogts),len(bogts))
bogdat = bog['temperatura'].tolist()

calts = cal['fecha'].tolist()
caltsint = np.linspace(0,len(calts),len(calts))
caldat = cal['temperatura'].tolist()

bucts = buc['fecha'].tolist()
buctsint = np.linspace(0,len(bucts),len(bucts))
bucdat = buc['temperatura'].tolist()

barts = bar['fecha'].tolist()
bartsint = np.linspace(0,len(barts),len(barts))
bardat = bar['temperatura'].tolist()

ipits = ipi['fecha'].tolist()
ipitsint = np.linspace(0,len(ipits),len(ipits))
ipidat = ipi['temperatura'].tolist()

#para bogota
plt.figure(figsize=(17,5))
f = interpolate.interp1d(bogtsint,bogdat)
f2 = interpolate.interp1d(bogtsint,bogdat,kind='cubic')
tck = interpolate.splrep(bogtsint,bogdat, s=0)
xnew = np.arange(0,len(bogts),0.1)
f3 = interpolate.splev(xnew, tck, der=0)
plt.plot(bogtsint,bogdat, "ko",xnew,f(xnew),'-r',xnew,f2(xnew),'--g',xnew,f3,'c')
plt.legend(['Datos', 'Lineal', 'Polinomio 3' ,'Splines 3'], loc='best')
plt.xlim(0,len(bogts))
plt.title('Cambios de temperatura a traves del tiempo en Bogota', fontsize=20)
plt.show()

# para Cali
plt.figure(figsize=(17,5))
f = interpolate.interp1d(caltsint,caldat)
f2 = interpolate.interp1d(caltsint,caldat,kind='cubic')
tck = interpolate.splrep(caltsint,caldat, s=0)
xnew = np.arange(0,len(calts),0.1)
f3 = interpolate.splev(xnew, tck, der=0)
plt.plot(caltsint,caldat, "ko",xnew,f(xnew),'-r',xnew,f2(xnew),'--g',xnew,f3,'c')
plt.legend(['Datos', 'Lineal', 'Polinomio 3' ,'Splines 3'], loc='best')
plt.xlim(0,len(calts))
plt.title('Cambios de temperatura a traves del tiempo en Cali', fontsize=20)
plt.show()

#para barranquilla
plt.figure(figsize=(17,5))
f = interpolate.interp1d(bartsint,bardat)
f2 = interpolate.interp1d(bartsint,bardat,kind='cubic')
tck = interpolate.splrep(bartsint,bardat, s=0)
xnew = np.arange(0,len(barts),0.1)
f3 = interpolate.splev(xnew, tck, der=0)
plt.plot(bartsint,bardat, "ko",xnew,f(xnew),'-r',xnew,f2(xnew),'--g',xnew,f3,'c')
plt.legend(['Datos', 'Lineal', 'Polinomio 3' ,'Splines 3'], loc='best')
plt.xlim(0,len(barts))
plt.title('Cambios de temperatura a traves del tiempo en Barranquilla', fontsize=20)
plt.show()

#Para Bucaramanga
plt.figure(figsize=(17,5))
f = interpolate.interp1d(buctsint,bucdat)
f2 = interpolate.interp1d(buctsint,bucdat,kind='cubic')
tck = interpolate.splrep(buctsint,bucdat, s=0)
xnew = np.arange(0,len(bucts),0.1)
f3 = interpolate.splev(xnew, tck, der=0)
plt.plot(buctsint,bucdat, "ko",xnew,f(xnew),'-r',xnew,f2(xnew),'--g',xnew,f3,'c')
plt.legend(['Datos', 'Lineal', 'Polinomio 3' ,'Splines 3'], loc='best')
plt.xlim(0,len(bucts))
plt.title('Cambios de temperatura a traves del tiempo en Bucaramanga', fontsize=20)
plt.show()

#para Ipiales
plt.figure(figsize=(17,5))
f = interpolate.interp1d(ipitsint,ipidat)
f2 = interpolate.interp1d(ipitsint,ipidat,kind='cubic')
tck = interpolate.splrep(ipitsint,ipidat, s=0)
xnew = np.arange(0,len(ipits),0.1)
f3 = interpolate.splev(xnew, tck, der=0)
plt.plot(ipitsint,ipidat, "ko",xnew,f(xnew),'-r',xnew,f2(xnew),'--g',xnew,f3,'c')
plt.legend(['Datos', 'Lineal', 'Polinomio 3' ,'Splines 3'], loc='best')
plt.xlim(0,len(ipits))
plt.title('Cambios de temperatura a traves del tiempo en ipiales', fontsize=20)
plt.show()


