import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Asia03 = pd.read_excel('IMVA.xls', sheet_name='IMVA')
print(Asia03)
print(Asia03.columns)

df_AsiaCountries03 = Asia03[['Periods', "Americas", "Canada", "USA", "Other Markets In Americas", "Oceania", "Australia", "New Zealand", "Other Markets In Oceania", "Africa", "Egypt", "Mauritius", "South Africa (Rep Of)", "Other Markets In Africa"]]
print(df_AsiaCountries03)

new = df_AsiaCountries03['Periods'].str.split(' ', n=1, expand=True)
df_AsiaCountries03 = df_AsiaCountries03.assign(Year=new[0])

print('->>>>><<<<<-Splitted Year->>>>><<<<<-')
df_AsiaCountries03['Year'] = pd.to_numeric(df_AsiaCountries03['Year'])
pd1 = df_AsiaCountries03['Year'].dtypes
print("Year type is", pd1)

print("->>>>><<<<<-dropped periods->>>>><<<<<-")
print(df_AsiaCountries03.drop(['Periods'], axis=1))
df_AsiaCountries33 = df_AsiaCountries03[(df_AsiaCountries03['Year'] >= 2011) & (df_AsiaCountries03['Year'] <= 2020)]

print('->>>>><<<<<-df_AsiaCountries33->>>>><<<<<-')
print(df_AsiaCountries33)

df_AsiaCountries04 = df_AsiaCountries33[["Americas", "Canada", "USA", "Other Markets In Americas", "Oceania", "Australia", "New Zealand", "Other Markets In Oceania", "Africa", "Egypt", "Mauritius", "South Africa (Rep Of)", "Other Markets In Africa"]]
print('-------df_AsiaCountries04-----')
print(df_AsiaCountries04)
print('sorted')

df_AsiaCountries05 = df_AsiaCountries04.replace(',', '', regex=True)
df_AsiaCountries06 = df_AsiaCountries05.replace('na', '0', regex=True)

print('->>>>><<<<<-df_AsiaCountries06->>>>><<<<<-')
print(df_AsiaCountries06)
df_AsiaCountries07 = df_AsiaCountries06.astype(int)
print(df_AsiaCountries07.dtypes)
psNotSorted=df_AsiaCountries07.sum()
psSorted = df_AsiaCountries07.sum().sort_values(ascending=False)

print('->>>>><<<<<-sorted->>>>><<<<<-')
print(psSorted)
allCountries = psSorted

print('->>>>><<<<<-Top 3 countries->>>>><<<<<-')
top3countries = psSorted.head(3)
print(top3countries)
total=top3countries.values.sum()
mean=round(top3countries.values.mean(),2)

print("The total no. of visitors for the top 3 countries is ",total)
print("The mean value for the top 3 countries is ",mean)


indexAll = np.arange(len(allCountries.index))


plt.figure(figsize=(10, 10))
plt.title('All other Countries from(Period:2011-2020)')
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(indexAll, allCountries.index, fontsize=6, rotation=30)
plt.bar(allCountries.index, allCountries.values / 1000)
plt.show()

indexAll = np.arange(len(allCountries.index))

plt.figure(figsize=(10, 10))
plt.xlabel('Countries', fontsize=8)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(indexAll, allCountries.index, fontsize=6, rotation=30)
plt.bar(top3countries.index, top3countries.values / 1000)
plt.show()

