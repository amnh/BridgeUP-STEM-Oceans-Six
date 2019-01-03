from netCDF4 import Dataset #Tool we need to load in our nc dataset
import numpy as np
import matplotlib.pyplot as plt
dataset = Dataset('/Users/katyabbott/Documents/GitHub/BridgeUP-STEM-Oceans-Six/datasets/Bermuda_data_SLA.nc')  #Loading in our dataset

print(dataset.variables)
dataset.variables.keys()

dataset.variables['sla'][:].shape
dataset.variables['time'][:].shape

lat = dataset.variables['latitude']
lon = dataset.variables['longitude']
sla = dataset.variables['sla']

day = 9148
graph = plt.pcolor(lon[:], lat[:], sla[day,:,:], cmap ='plasma')
cb = plt.colorbar(graph)
cb.set_label('m')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title('Sea level anomaly in Bermuda on day 9149')
plt.savefig('sla_Bermuda_9149.png', format = 'png', dpi = 1000)


