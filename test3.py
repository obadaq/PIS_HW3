import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


crime_spain_df = pd.read_csv('crime_rate_Spain.csv')



crimes = list(set(crime_spain_df['Crime']))
years = list(set(crime_spain_df['Year']))
locations = list(set(crime_spain_df['Location']))
tc= crime_spain_df.groupby('Location').sum()['Total cases']


# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar

crime1_tc_bylocation = crime_spain_df[crime_spain_df['Crime']== crimes[0]].groupby('Location').sum()
crime2_tc_bylocation = crime_spain_df[crime_spain_df['Crime']== crimes[1]].groupby('Location').sum()
crime3_tc_bylocation = crime_spain_df[crime_spain_df['Crime']== crimes[2]].groupby('Location').sum()

# Set position of bar on X axis

br1 = np.arange(len(crime1_tc_bylocation))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, crime1_tc_bylocation, color ='r', width = barWidth,
        edgecolor ='grey', label =crimes[0])
plt.bar(br2, crime2_tc_bylocation, color ='g', width = barWidth,
        edgecolor ='grey', label =crimes[1])
plt.bar(br3, crime3_tc_bylocation, color ='b', width = barWidth,
        edgecolor ='grey', label =crimes[2])


# Adding Xticks
plt.xlabel('Locations', fontweight ='bold', fontsize = 15)
plt.ylabel('Total Cases', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(crime1_tc_bylocation))],
        locations)
 
plt.legend()
plt.show()