import pandas as pd
import shutil
import os

dataFolderPath = './data'

if os.path.exists(dataFolderPath):
  shutil.rmtree(dataFolderPath)

os.mkdir(dataFolderPath)

uzorciNovi = pd.read_csv('./Svi uzorci NOVI.csv')

grouped = uzorciNovi.sort_values(by='Analysis', ascending=True)

#for this dummy only - FOR TESTING ONLY
grouped.to_csv('./data/GRUPISANI.csv')


# filtering is done here
filteredSamples = grouped.loc[
  (grouped['TOC(%)'] > 0.5) & 
  (grouped['Tmax(°C)'] > 400) &
  (grouped['HI'] > 500) 
]

filteredSamples.to_csv('./data/filtrirani.csv')

# print(filteredSamples)
print('SCRIPT FINISHED')



