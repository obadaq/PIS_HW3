'''
Assignment #3
Data source: https://www.kaggle.com/datasets/marshuu/crime-rate-in-spain-2019-2021
Generate plots showing:
1.The trend of a phenomenon (e.g., specific crime) over time.
2.A pie chart showing the distribution of different crimes in the country or in a  specific city
3.A bar chart showing a comparison of the number of some crimes (e.g. three crimes) in a few cities (at least five)
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', 20)
pd.set_option('display.width', None)

# Reading Data
crime_df = pd.read_csv("crime_rate_Spain.csv")


# Creating a list of crime names to use it in a menu for the user to choose from
crime_names = list(set(crime_df["Crime"].values))
##############################################################################################################
# First Plot: showing The trend of a phenomenon (e.g., specific crime) over time.
##############################################################################################################
#

print("Enter the crime number to plot its trend: ")
for i in range(len(crime_names)):
    print(i + 1, " )", crime_names[i])

index = int(input("Crime Number: "))
specific_crime_name = crime_names[index - 1]

# Creating sub data frame containing only the rows having a specific crime chosen by the user a specific
specific_crime_df = crime_df[crime_df["Crime"] == specific_crime_name]

# grouping the sub data frame of the specific crime by year
specific_crime_group_by_year = specific_crime_df[["Year", "Total cases"]].groupby("Year")

# Plotting the required chart
fig, ax = plt.subplots()
ax.set(xlabel='Year', ylabel='Total Cases', title=specific_crime_name + ' Crime Trend')
ax.set_xticks(list(range(2015, 2025)))
y = specific_crime_group_by_year.sum()["Total cases"]
x = y.index
ax.plot(x, y, x, y, "or")
plt.show()

##############################################################################################################
# Second Plot : A pie chart showing the distribution of different crimes in the country or in a  specific city
##############################################################################################################
# Creating a list of city names to use it in a menu for the user to choose from
city_names = list(set(crime_df["Location"].values))
print("Enter the city to plot a pie chart showing the distribution of different crimes in it : ")
for i in range(len(city_names)):
    print(i + 1, " )", city_names[i])
index = int(input("City Number: "))
specific_city_name = city_names[index - 1]

# Creating sub data frame containing only the rows having a specific city chosen by the user a specific
specific_city_df = crime_df[crime_df["Location"] == specific_city_name]
# grouping the sub data frame of the specific city by crime
specific_city_group_by_crime = specific_city_df[["Crime", "Total cases"]].groupby("Crime")
# Plotting the required chart
fig, ax = plt.subplots()
fig.set_size_inches(12,5)

ax.pie(specific_city_group_by_crime.sum()["Total cases"], radius=1)
ax.set_title("Distribution of different crimes in " + specific_city_name)
ax.legend(labels=crime_names, prop={'size': 8}, bbox_to_anchor=(1, .5, .07, .06))
plt.show()
################################################################################################################################
# Third Plot: A bar chart showing a comparison of the number of some crimes (e.g. three crimes) in a few cities (at least five)
################################################################################################################################

city_names = ["Barcelona", "Valencia", "Murcia", "Madrid", "Spain"]
specific_crime_names = ["Vehicle theft", "Theft", "Robberies with force in homes"]
x = np.arange(len(city_names))
width = 0.09
fig, ax = plt.subplots()
# Creating sub data frame containing rows of the 5 cities in the city_names list having the first crime in specific_crime_names list
specific_cities_crimes_df = crime_df[((crime_df["Location"] == city_names[0]) | (
        crime_df["Location"] == city_names[1]) | (crime_df["Location"] == city_names[2]) | (
                                              crime_df["Location"] == city_names[3]) | (
                                              crime_df["Location"] == city_names[4])) & (
                                             crime_df["Crime"] == specific_crime_names[0])]
# Creating sub data frame containing rows of the 5 cities in the city_names list having the second crime in specific_crime_names list
specific_cities_crimes_df2 = crime_df[((crime_df["Location"] == city_names[0]) | (
        crime_df["Location"] == city_names[1]) | (crime_df["Location"] == city_names[2]) | (
                                               crime_df["Location"] == city_names[3]) | (
                                               crime_df["Location"] == city_names[4])) & (
                                              crime_df["Crime"] == specific_crime_names[1])]
# Creating sub data frame containing rows of the 5 cities in the city_names list having the third crime in specific_crime_names list
specific_cities_crimes_df3 = crime_df[((crime_df["Location"] == city_names[0]) | (
        crime_df["Location"] == city_names[1]) | (crime_df["Location"] == city_names[2]) | (
                                               crime_df["Location"] == city_names[3]) | (
                                               crime_df["Location"] == city_names[4])) & (
                                              crime_df["Crime"] == specific_crime_names[2])]
# First bar showing the first crime's total cases of the 5 cities
ax.bar(x - width, specific_cities_crimes_df[["Location", "Total cases"]].groupby("Location").sum()["Total cases"],
       width, label=specific_crime_names[0], color="green")
# Second bar showing the second crime's total cases of the 5 cities
ax.bar(x, specific_cities_crimes_df2[["Location", "Total cases"]].groupby("Location").sum()["Total cases"], width,
       label=specific_crime_names[1], color="red")
# Third bar showing the third crime's total cases of the 5 cities
ax.bar(x + width, specific_cities_crimes_df3[["Location", "Total cases"]].groupby("Location").sum()["Total cases"],
       width, label=specific_crime_names[2], color="black")

ax.set_ylabel('Total Cases')
ax.set_title('Comparison of number of Crimes in a few Cities')
ax.set_xticks(x)
ax.set_xticklabels(city_names, rotation='horizontal')
ax.legend()
fig.tight_layout()
plt.show()