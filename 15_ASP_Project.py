import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.read_excel("IMVA.xls", sheet_name="IMVA")
# data = dates['Periods'].str.split(' ', n=1, expand = True)
# dates = dates.assign(month=data[1])
# dates.index = dates["month"]
print(dates)
print(dates.columns)
newdata = {'Countries':['Americas', 'Canada', 'USA', 'Other Markets In Americas', 'Oceania', 'Australia', 'New Zealand', 'Other Markets In Oceania', 'Africa', 'Egypt', 'Mauritius', 'South Africa (Rep of)', 'Other Markets In Africa']}
df = pd.DataFrame(newdata)
df = [['Countries']]
print(df)