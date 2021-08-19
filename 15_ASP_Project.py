import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Others03 = pd.read_excel('IMVA.xls', sheet_name='IMVA')
# print(Others03)
# print(Others03.columns)

df_OthersCountries03 = Others03[['Periods', "Americas", "Canada", "USA", "Other Markets In Americas", "Oceania", "Australia", "New Zealand", "Other Markets In Oceania", "Africa", "Egypt", "Mauritius", "South Africa (Rep Of)", "Other Markets In Africa"]]
# print(df_OthersCountries03.columns)
# print(df_OthersCountries03)

new = df_OthersCountries03['Periods'].str.split(' ', n=1, expand=True)
df_OthersCountries03 = df_OthersCountries03.assign(Year=new[0])

print('->>>>><<<<<-Splitted Year->>>>><<<<<-')
df_OthersCountries03['Year'] = pd.to_numeric(df_OthersCountries03['Year'])
pd1 = df_OthersCountries03['Year'].dtypes
print("Year type is", pd1)

print("->>>>><<<<<-Dropped Periods->>>>><<<<<-")
print(df_OthersCountries03.drop(['Periods'], axis=1))
df_OthersCountries33 = df_OthersCountries03[(df_OthersCountries03['Year'] >= 2011) & (df_OthersCountries03['Year'] <= 2020)]

print('->>>>><<<<<-df_OthersCountries33->>>>><<<<<-')
print(df_OthersCountries33)
print(df_OthersCountries33.head(3))
print(df_OthersCountries33.tail(3))

df_OthersCountries04 = df_OthersCountries33[["Americas", "Canada", "USA", "Other Markets In Americas", "Oceania", "Australia", "New Zealand", "Other Markets In Oceania", "Africa", "Egypt", "Mauritius", "South Africa (Rep Of)", "Other Markets In Africa"]]
print('-------df_OthersCountries04-----')
print(df_OthersCountries04)
print('sorted')

df_OthersCountries05 = df_OthersCountries04.replace(',', '', regex=True)
df_OthersCountries06 = df_OthersCountries05.replace('na', '0', regex=True)

print('->>>>><<<<<-df_OthersCountries06->>>>><<<<<-')
print(df_OthersCountries06)
df_OthersCountries07 = df_OthersCountries06.astype(int)
print(df_OthersCountries07.dtypes)
psNotSorted=df_OthersCountries07.sum()
psSorted = df_OthersCountries07.sum().sort_values(ascending=False)

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


# plt.figure(figsize=(10, 10))
# plt.title('All other Countries from(Period:2011-2020)')
# plt.xlabel('Countries', fontsize=8)
# plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
# plt.xticks(indexAll, allCountries.index, fontsize=6, rotation=30)
# plt.bar(allCountries.index, allCountries.values / 1000)
# plt.show()
#
# indexAll = np.arange(len(allCountries.index))
#
# plt.figure(figsize=(10, 10))
# plt.title('Top 3 Countries from(Period:2011-2020)')
# plt.xlabel('Countries', fontsize=8)
# plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
# plt.xticks(indexAll, allCountries.index, fontsize=6, rotation=30)
# plt.bar(top3countries.index, top3countries.values / 1000)
# plt.show()

