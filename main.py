import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

crime_spain_df = pd.read_csv('crime_rate_Spain.csv')

crimes = list(set(crime_spain_df['Crime']))
years = list(set(crime_spain_df['Year']))
locations = list(set(crime_spain_df['Location']))


def plot_trend():
    i = 1
    for crime in crimes:
        print(i , ' - ' , crime)
        i += 1 
        
    user_ch = int(input('Enter a crime no. to show the trend for >> '))
    tc = crime_spain_df[crime_spain_df['Crime'] == crimes[user_ch - 1]].groupby('Year').sum()['Total cases']

    plt.xlabel='Year'
    plt.ylabel='Total Cases' 
    plt.xticks(years)
    plt.title='Crimes in Spain Over Three Years'
    plt.plot(years, tc, "or", years, tc, label= crimes[user_ch - 1])
    plt.show()


def plot_pie(location):

    total_loc_cases = crime_spain_df[crime_spain_df['Location'] == location].groupby('Crime').sum()['Total cases']

    fig, ax = plt.subplots()
    ax.pie(total_loc_cases, radius=1, wedgeprops=dict(width=0.3, edgecolor='white'))
    ax.legend(crimes, loc=2)
    ax.set_title = "Crimes in" + location
    plt.show()


def plot_bars():

    a1 = crime_spain_df.groupby(['Location']).sum()['Total cases']
    plt.xlabel('Locations')
    plt.ylabel('Total Cases')
    plt.title('Crimes in Spain"By City"')
    plt.xticks(np.arange(len(locations)), rotation=45)
    plt.bar(locations, a1)
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
elif user_ch == 2:
    print(locations)
    user_ch = input("Write a location to sho its data >>>  ")
    plot_pie(user_ch)
else:
    print("Run again ??")
