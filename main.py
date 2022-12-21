import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

crime_spain_df = pd.read_csv('crime_rate_Spain.csv')
crime_US_df = pd.read_csv('US_violent_crime.csv')
crimes = list(set(crime_spain_df['Crime']))
years = list(set(crime_spain_df['Year']))
locations = list(set(crime_spain_df['Location']))
a1 = crime_spain_df.groupby(['Location']).sum()['Total cases']

def plot_trend():
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

def plot_pie(location):

        total_loc_cases= crime_spain_df[crime_spain_df['Location']==location].groupby('Crime').sum()['Total cases']

        fig, ax = plt.subplots()
        ax.pie(total_loc_cases,radius=1.2)
        ax.legend(crimes,loc=2)
        plt.show()

def plot_bars():
        plt.xlabel('Locations')
        plt.ylabel('Total Cases')
        plt.title('Crimes in Spain"By City"')
        plt.xticks(np.arange(len(locations)),rotation=45)
        plt.bar(locations,a1)
        plt.show()

print('''
1. show trends for crimes in spain (2019-2021)
2. show pie chart for crimes in a city of your choice
3. show bar chart for total crimes in spain in general
''')
user_ch = int(input('Enter your choice >>> '))

if user_ch == 1:
        plot_trend()
elif user_ch == 3:
        plot_bars()
elif user_ch==2:
        print(locations)
        user_ch = input("Write a location to sho its data >>>  ")
        plot_pie(user_ch)
else: print("Run again ??")











