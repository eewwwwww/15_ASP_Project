import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.read_excel("IMVA.xls", sheet_name="IMVA")
newdata = dates[["Americas", "Canada", "USA", "Other Markets In Americas", "Oceania", "Australia", "New Zealand", "Other Markets In Oceania", "Africa", "Egypt", "Mauritius", "South Africa (Rep Of)", "Other Markets In Africa"]]
print(newdata.columns)
data = dates['Periods'].str.split(' ', n=1, expand = True)
dates = dates.assign(Year="Periods"[1])
dates.index = dates["Year"]
print(dates)
# q1 = dates[(dates["Year"] >= str(2011)) & (dates["Year"] <= str(2020))]
# df = pd.DataFrame(newdata)
# print(df)
# print(df.head(3))
# print(df.tail(3))
