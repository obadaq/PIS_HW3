import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


crime_spain_df = pd.read_csv('crime_rate_Spain.csv')
crime_US_df = pd.read_csv('US_violent_crime.csv')


crimes = list(set(crime_spain_df['Crime']))
years = list(set(crime_spain_df['Year']))
locations = list(set(crime_spain_df['Location']))
tc= crime_spain_df[crime_spain_df['Location']==locations[1]].groupby('Crime').sum()['Total cases']


fig, ax = plt.subplots()
startx, endx = min(years), max(years)
starty, endy = min(list(crime_spain_df.groupby('Crime').sum()['Total cases'])), max(list(crime_spain_df.groupby('Crime').sum()['Total cases']))

ax.set(xlabel='Year',
       ylabel= 'Total Cases',
       title='Crimes in Spain Over Three Years')
ax.set_xticks(years)

for crime in crimes:
        tc = crime_spain_df[crime_spain_df['Crime']==crime].groupby('Year').sum()['Total cases']
        ax.plot(years,tc,label=crime)

ax.legend(loc='best')
plt.show()

fig1, ax1 = plt.subplots()
ax1.pie(tc,radius=1,labels=crimes)
ax1.legend(loc=2)
plt.show()


