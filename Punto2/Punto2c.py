
# coding: utf-8


from netCDF4 import Dataset														# Libreria para leer .nc
import matplotlib.pyplot as pyplot												# pyplot
import matplotlib.pylab as plt

file1 = 'air.mon.ltm.nc'														# Nombre del archivo
nc1 = Dataset(file1, mode='r')													# Abrir el archivo en modo lectura

air = nc1.variables['air']														# Llamando columna air
lon = nc1.variables['lon']														# Llamando columna lon
lat = nc1.variables['lat']														# Llanmando columna lat
lonvals = lon[:]																# los valores de la columna lon
latvals = lat[:]																# los valores de la columna lat
temp = air[0]																	# temperatura media del aire


plt.figure(figsize=(15,5))														# Creando figura
plt.imshow(temp, cmap=plt.get_cmap('spectral'), interpolation ='nearest') 		# Imshow  "nearest neighbour" interpolation
plt.colorbar()																	# Añadiendo una escala de valores
plt.title (air.long_name + ' (' + air.units + ')')								# Titulo
plt.xlabel(lon.long_name    + ' (' + lon.units    + ')')						# Nombrando al eje x
plt.ylabel(lat.long_name    + ' (' + lat.units    + ')')						# Nombrando al eje y
plt.savefig('nearestn.png')																		# Mostrando el grafico


