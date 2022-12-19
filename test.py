import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


crime_spain_df = pd.read_csv('crime_rate_Spain.csv')
crime_US_df = pd.read_csv('US_violent_crime.csv')


crimes = list(set(crime_spain_df['Crime']))
years = list(set(crime_spain_df['Year']))
locations = list(set(crime_spain_df['Location']))
tc= crime_spain_df[crime_spain_df['Location']==locations[5]].groupby('Crime').sum()['Total cases']


fig, ax = plt.subplots()
ax.pie(tc,radius=1.2)
ax.legend(loc=2)
plt.show()
print(tc)