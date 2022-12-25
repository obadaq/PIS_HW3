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
        print(i, ' - ', crime)
        i += 1 
        
    user_ch = int(input('Enter a crime no. to show the trend for >> '))
    tc = crime_spain_df[crime_spain_df['Crime'] == crimes[user_ch - 1]].groupby('Year').sum()['Total cases']

    plt.xlabel('Year')
    plt.ylabel('Total Cases') 
    plt.xticks(years)
    plt.title(crimes[user_ch - 1]+' in Spain Over Three Years')
    plt.plot(years, tc, "or", years, tc, label=crimes[user_ch - 1])
    plt.show()


def plot_pie(location):

    total_loc_cases = crime_spain_df[crime_spain_df['Location'] == location].groupby('Crime').sum()['Total cases']

    fig, ax = plt.subplots()
    ax.pie(total_loc_cases, radius=1, wedgeprops=dict(width=0.3, edgecolor='white'))
    ax.legend(crimes, loc=2)
    ax.set_title("Crimes in " + location)
    plt.show()


def plot_bars():

    barWidth = 0.25
    fig, axes = plt.subplots(2, 1)
 
    crime1_tc_bylocation = crime_spain_df[crime_spain_df['Crime'] == crimes[0]].groupby('Location').sum()['Total cases']
    crime2_tc_bylocation = crime_spain_df[crime_spain_df['Crime'] == crimes[1]].groupby('Location').sum()['Total cases']
    crime3_tc_bylocation = crime_spain_df[crime_spain_df['Crime'] == crimes[2]].groupby('Location').sum()['Total cases']

    br1 = np.arange(len(crime1_tc_bylocation))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]

    axes[0].bar(br1, crime1_tc_bylocation, color='r', width=barWidth, edgecolor='grey', label=crimes[0])
    axes[0].bar(br1, crime2_tc_bylocation, bottom=crime1_tc_bylocation, color='g', width=barWidth,
                edgecolor='grey', label=crimes[1])
    axes[0].bar(br1, crime3_tc_bylocation, bottom=crime2_tc_bylocation+crime1_tc_bylocation, color='b', width=barWidth,
                edgecolor='grey', label=crimes[2])

    axes[0].set_xlabel('Locations', fontweight='bold', fontsize=15)
    axes[0].set_ylabel('Total Cases', fontweight='bold', fontsize=15)
    axes[0].set_xticks([r + barWidth for r in range(len(crime1_tc_bylocation))], locations, rotation=45)
    axes[0].set_title('Crime Comparison in Spain', fontweight='bold')
    axes[0].legend()

    axes[1].bar(br1, crime1_tc_bylocation, color='r', width=barWidth, edgecolor='grey', label=crimes[0])
    axes[1].bar(br2, crime2_tc_bylocation, color='g', width=barWidth, edgecolor='grey', label=crimes[1])
    axes[1].bar(br3, crime3_tc_bylocation, color='b', width=barWidth, edgecolor='grey', label=crimes[2])
    axes[1].set_xlabel('Locations', fontweight='bold', fontsize=15)
    axes[1].set_ylabel('Total Cases', fontweight='bold', fontsize=15)
    axes[1].set_xticks([r + barWidth for r in range(len(crime1_tc_bylocation))], locations, rotation=45)
    plt.show()


print('''
1. show trends for crimes in spain (2019-2021)
2. show pie chart for crimes in a city of your choice
3. show bar chart for total cases in spain with three RANDOM crimes 
''')
user_sel = int(input('Enter your choice >>> '))

if user_sel == 1:
    plot_trend()
elif user_sel == 3:
    plot_bars()
elif user_sel == 2:
    print(locations)
    user_sel = input("Write a location to sho its data >>>  ")
    plot_pie(user_sel)
else:
    print("Run again ??")