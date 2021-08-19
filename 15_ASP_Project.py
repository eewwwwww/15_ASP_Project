import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# dates = pd.read_excel("IMVA.xls", sheet_name="IMVA")
# newdata = dates[["Americas", "Canada", "USA", "Other Markets In Americas", "Oceania", "Australia", "New Zealand", "Other Markets In Oceania", "Africa", "Egypt", "Mauritius", "South Africa (Rep Of)", "Other Markets In Africa"]]
# print(newdata.columns)
# data = dates['Periods'].str.split(' ', n=1, expand = True)
# dates = dates.assign(Year="Periods"[1])
# dates.index = dates["Year"]
# print(dates)
# q1 = dates[(dates["Year"] >= str(2011)) & (dates["Year"] <= str(2020))]
# df = pd.DataFrame(newdata)
# print(df)
# df1 = dates['Periods'].str.split(' ', n=1, expand = True)
# print(df1)
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
class Visitors:
    dataframe = pd.read_excel('IMVA.xls', sheet_name = 'IMVA')
    dataframe2 = dataframe[['Periods', "Americas", "Canada", "USA", "Other Markets In Americas", "Oceania", "Australia", "New Zealand", "Other Markets In Oceania", "Africa", "Egypt", "Mauritius", "South Africa (Rep Of)", "Other Markets In Africa" ]]
    print(dataframe2.columns)
    new = dataframe2['Periods'].str.split(' ', n=1, expand=True)
    dataframe2 = dataframe2.assign(Year=new[0])
    dataframe2['Year'] = pd.to_numeric(dataframe2['Year'])
    pd1 = dataframe2['Year'].dtypes
    dataframe3 = dataframe2[(dataframe2['Year'] >= 2011) & (dataframe2['Year'] <= 2020)]
    print(dataframe3)
    print(dataframe3.head(3))
    print(dataframe3.tail(3))
    print(sorted(dataframe3))