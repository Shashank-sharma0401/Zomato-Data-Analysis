import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataframe = pd.read_csv("Zomato data .csv")
print(dataframe)
def handleRate(value):
    value = str(value).split('/')
    value = value[0];
    return float(value)
dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head())
dataframe.info
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of restaurant")
plt.show()
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result , c="green",marker="o")
plt.xlabel("Type of restaurant",c="red",size=20)
plt.ylabel("Votes",c="red",size=20)
plt.hist(dataframe['rate'],bins=7)
plt.title("ratings distribution")
plt.show()
couple_data =  dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.show()
plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)
pivot_table = dataframe.pivot_table(index = 'listed_in(type)' , columns = 'online_order' , aggfunc = 'size' , fill_value = 0)
sns.heatmap(pivot_table , annot = True, cmap = "YlGnBu" , fmt = 'd')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()
