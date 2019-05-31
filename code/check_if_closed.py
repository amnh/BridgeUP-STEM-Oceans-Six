from netCDF4 import Dataset #Tool we/Users/student/Desktop/BridgeUP-STEM-Abbott/labs/eddy_contours_script_032819.py need to load in our nc dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = Dataset('../datasets/Bermuda_data_SLA.nc')  #Loading in our dataset
lat = dataset.variables['latitude']
lon = dataset.variables['longitude']
sla = dataset.variables['sla']

from matplotlib.path import Path
##the first path should return true
path1 = Path([(295.18448575, 32.),(295.19526986, 32.2),(295.2, 32.20979566),(295.20711855, 32.2),(295.18448575, 32.)], None)
##the second path should return false
path2 = Path([(291.18448575, 22.),(295.19526986, 32.2),(295.2, 32.20979566),(295.20711855, 32.2),(295.23659369, 32.)], None)

plt.plot(path1.vertices[:,1], path1.vertices[:,0])

sum(abs(path1.vertices[0] - path1.vertices[-1]))


path1.vertices[0] - path1.vertices[-1]


cp = plt.contour(lon[:], lat[:], sla[0])
cp.levels
coll = cp.collections
df = pd.DataFrame()
for i, obj in enumerate(coll):
    paths = obj.get_paths()
    level = cp.levels[i]
    for path in paths:
        df_temp = pd.DataFrame({'level': level, 'path': path}, index = [0])
        df = df.append(df_temp, ignore_index = True)


def if_closed(contour):
    if sum(abs(contour.vertices[0] - contour.vertices[-1])) < .005:
        return True
    else:
        return False


df['closed'] = df['path'].apply(if_closed)
df = df[df['closed'] == True]


row = df.iloc[0]
row1 = df.iloc[1]
row1['path'].contains_path(row['path'])

df_final = df.copy()
df_final['Contains'] = 0
for index, row in df_final.iterrows():
    for index1, row1 in df.iterrows():
        if not row1.equals(row):
            if row1['path'].contains_path(row['path']):
                df_final.loc[index, 'Contains'] = 1

df_final2 = df.copy()
for index, row in df_final2.iterrows():
    for index1, row1 in df.iterrows():
        if not row1.equals(row):
            if row1['path'].contains_path(row['path']):
                df_final2.loc[index, 'path'] = 0

for index, row in df_final2.iterrows():
    if df_final2['path'].apply(lambda x: x.contains_path(row['path'])).sum() > 0:
        df_final2.loc[index, 'Contains'] = 1

df_final2

df_final.loc[1, 'Contains']
counter

not row1.equals(row)


row1['path'].vertices[:,0]
