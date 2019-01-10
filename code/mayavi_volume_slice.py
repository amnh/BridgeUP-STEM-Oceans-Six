from netCDF4 import Dataset #Tool we need to load in our nc dataset
import numpy as np
import matplotlib.pyplot as plt
from mayavi import mlab

dataset = Dataset('/Users/katyabbott/Documents/GitHub/BridgeUP-STEM-Oceans-Six/datasets/Bermuda_data_SLA.nc')  #Loading in our dataset
lat = dataset.variables['latitude'][:]
lon = dataset.variables['longitude'][:]
sla = dataset.variables['sla'][:]
time = dataset.variables['time'][:]

time1 = (time - np.min(time))[20:31]  #subtract the minimum date from the time variables to plot from 0 days onward
sla1 = sla[20:31,:,:] #selecting only the 10-21st day of data because time variable is much longer than lat/lon and inconvenient to display
sla1 = np.transpose(sla1, (0,2,1)) #reorder with time on x, lon on y, lat on z axes

x, y, z = np.meshgrid(time1, lon, lat, indexing='ij') #create uniform nxmxp grids

xx = mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(x,y,z,sla1), plane_orientation='x_axes', slice_index=8, colormap = 'plasma')
yy = mlab.pipeline.image_plane_widget(mlab.pipeline.scalar_field(x,y,z,sla1), plane_orientation='y_axes', slice_index=10, colormap = 'plasma')
data = mlab.pipeline.volume(mlab.pipeline.scalar_field(x,y,z,sla1))

mlab.axes(xlabel='time', ylabel='longitude', zlabel='latitude', nb_labels=5) #creates axes labels and tick marks
mlab.outline() #creates a box around the figure
scalarbar = mlab.scalarbar() #adds colorbar
scalarbar.scalar_bar_representation.proportional_resize=True
mlab.show() #displays image in iPython window

sla.data
