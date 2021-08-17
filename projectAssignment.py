import numpy as np
import pandas as pd
import matplotlib.pyplot
import plot as plot
from matplotlib import pyplot as plt

data = pd.read_excel('dataNew.xls', sheet_name='data')
print(data)
dataSplit = data['Period'].str.split(' ', n=1, expand = True)
print(data.head(11))
dataSplit[1] = dataSplit[1].astype(str).astype(int)
print(dataSplit[1])
print(dataSplit.dtypes)
df1 = dataSplit[(dataSplit[1] >= 1900) & (dataSplit[1] <= 1910)]
print(df1[1])
plt.bar(df1[1], data["Calories"].head(11))
plt.xticks(df1[1])
plt.ylabel('Number of Calories')
plt.xlabel('Year')
plt.show()
print(round(data["Calories"].head(11).mean(), 2))
print(round(data["Calories"].head(11).sum(), 2)) #end of first bar chat

df2 = dataSplit[(dataSplit[1] >= 1911) & (dataSplit[1] <= 1920)]
print(df2[1])
plt.bar(df2[1], data[11:21]["Calories"])
plt.xticks(df2[1])
plt.ylabel('Number of Calories')
plt.xlabel('Year')
plt.show()
print(round(data[11:21]["Calories"].mean(), 2))
print(round(data[11:21]["Calories"].sum(), 2)) #end of second bar chat

df3 = dataSplit[(dataSplit[1] >= 1921) & (dataSplit[1] <= 1930)]
print(df3[1])
plt.bar(df3[1], data[21:31]["Calories"])
plt.xticks(df3[1])
plt.ylabel('Number of Calories')
plt.xlabel('Year')
plt.show()
print(round(data[21:31]["Calories"].mean(), 2))
print(round(data[21:31]["Calories"].sum(), 2)) #end of third bar chat

