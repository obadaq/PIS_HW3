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



# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
IT = [12, 30, 1, 8, 22]
ECE = [28, 6, 16, 5, 10]
CSE = [29, 3, 24, 25, 17]
 
# Set position of bar on X axis
br1 = np.arange(len(IT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, IT, color ='r', width = barWidth,
        edgecolor ='grey', label ='IT')
plt.bar(br2, ECE, color ='g', width = barWidth,
        edgecolor ='grey', label ='ECE')
plt.bar(br3, CSE, color ='b', width = barWidth,
        edgecolor ='grey', label ='CSE')
 
# Adding Xticks
plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(IT))],
        ['2015', '2016', '2017', '2018', '2019'])
 
plt.legend()
plt.show()