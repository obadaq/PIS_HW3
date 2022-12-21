import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


crime_spain_df = pd.read_csv('crime_rate_Spain.csv')
crime_US_df = pd.read_csv('US_violent_crime.csv')


crimes = list(set(crime_spain_df['Crime']))
years = list(set(crime_spain_df['Year']))
locations = list(set(crime_spain_df['Location']))
tc= crime_spain_df.groupby('Location').sum()['Total cases']


a1 = crime_spain_df.groupby(['Location']).sum()['Total cases']

plt.xlabel('Locations')
plt.ylabel('Total Cases')
plt.title('Crimes in Spain"By City"')
plt.xticks(np.arange(len(locations)),rotation=45)
#plt.yticks(np.linspace(100000,1500000,100000))
plt.bar(locations,a1)
plt.show()
