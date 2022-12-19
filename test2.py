import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


crime_spain_df = pd.read_csv('crime_rate_Spain.csv')
crime_US_df = pd.read_csv('US_violent_crime.csv')


crimes = list(set(crime_spain_df['Crime']))
years = list(set(crime_spain_df['Year']))
locations = list(set(crime_spain_df['Location']))
tc= crime_spain_df.groupby('Location').sum()['Total cases']

print(tc)

x = np.arange(len(locations))
width = 0.25
a1 = crime_spain_df[crime_spain_df['Location']==locations[1]].groupby('Crime').sum()['Total cases']
fig, ax = plt.subplots()
ax.bar(x-width/2, tc,width, label='locations[0]',color='red')
#ax.bar(x-width/2, a2,width, label=locations[0],color='red')

ax.set_xticks(x)
ax.set_xticklabels(locations, rotation='vertical')