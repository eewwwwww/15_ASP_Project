import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# dates = pd.read_excel('dataNew.xls')
# data = dates['Period'].str.split(' ', n=1, expand = True)
# dates = dates.assign(Year=data[1])
# dates.index = dates["Year"]
# print(dates)
#
# df1 = dates[(dates["Year"] >= str(1900)) & (dates["Year"] <= str(1910))]
# qs = df1["Calories"].sort_values();
# index = np.array(len(qs.index));
# plt.xlabel('Year')
# plt.ylabel('Number of Calories')
# plt.xticks(index, qs.index);
# plt.title('Data Sheet');
# plt.bar(qs.index, qs.values);
# print(plt.show())
# print(round(data["Calories"].head(11).mean(), 2))
# print(round(data["Calories"].head(11).sum(), 2)) #end of first bar chat
#
# df2 = newdata[(newdata[1] >= str(1911)) & (newdata[1] <= str(1920))]
# df2[1]["Calories"].sort_values()
# print(df2[1])
# plt.bar(df2[1], data[11:21]["Calories"])
# plt.xticks(df2[1])
# plt.ylabel('Number of Calories')
# plt.xlabel('Year')
# plt.show()
# print(round(data[11:21]["Calories"].mean(), 2))
# print(round(data[11:21]["Calories"].sum(), 2)) #end of second bar chat
#
# df3 = newdata[(newdata[1] >= 1921) & (newdata[1] <= 1930)]
# df3[1]["Calories"].sort_values()
# print(df3[1])
# plt.bar(df3[1], data[21:31]["Calories"])
# plt.xticks(df3[1])
# plt.ylabel('Number of Calories')
# plt.xlabel('Year')
# plt.show()
# print(round(data[21:31]["Calories"].mean(), 2))
# print(round(data[21:31]["Calories"].sum(), 2)) #end of third bar chat
datas = pd.read_excel('datanew.xls')
data = datas['Period'].str.split(' ',n=1, expand=True)

datas = datas.assign(Year=data[1])
datas.index = datas["Year"]
print(datas)

q1 = datas[(datas["Year"] >= str(1900)) & (datas["Year"] <= str(1910))]
q2 = datas[(datas["Year"] >= str(1911)) & (datas["Year"] <= str(1921))]
q3 = datas[(datas["Year"] >= str(1921)) & (datas["Year"] <= str(1931))]

ps = q1['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Period');
plt.ylabel('Calories');
plt.xticks(index, ps.index);
plt.title('Data Sheet');
plt.bar(ps.index,ps.values);
plt.show();
print(round(datas["Calories"].head(11).mean(), 2))
print(round(datas["Calories"].head(11).sum(), 2))#end of first bar chat

ps = q2['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Period');
plt.ylabel('Calories');
plt.xticks(index, ps.index);
plt.title('Data Sheet');
plt.bar(ps.index,ps.values);
plt.show();
print(round(datas[11:21]["Calories"].mean(), 2))
print(round(datas[11:21]["Calories"].sum(), 2))

ps = q3['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Period');
plt.ylabel('Calories');
plt.xticks(index, ps.index);
plt.title('Data Sheet');
plt.bar(ps.index,ps.values);
plt.show();
print(round(datas[21:31]["Calories"].mean(), 2))
print(round(datas[21:31]["Calories"].sum(), 2))