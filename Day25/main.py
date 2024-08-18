# with open("weather_data.csv", "r") as weather_data:
#     data = weather_data.readlines()
#
# print(data)
#
# import csv
#
# import pandas
# import pandas as pd
#
# columns = []
# with open("weather_data.csv", "r") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)
# data = pd.read_csv("weather_data.csv")
# print(type(data))
# temp = data["temp"]
#
# print(temp.mean())
# print(temp.max())
# print(data["condition"])
#
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == temp.max()])
#
# monday_temp = data[data["day"] == "Monday"]["temp"]
# print(monday_temp)
# monday_temp = monday_temp * 1.8 + 32
# print(monday_temp)
#
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# dataframe_dict = pandas.DataFrame(data_dict)
# dataframe_dict.to_csv("new_data.csv")

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240729.csv")
print(data)
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# color_value_count = data["Primary Fur Color"].value_counts()['Black']
print(grey_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

dic_dataframe = pd.DataFrame(data_dict)
print(dic_dataframe)
dic_dataframe.to_csv("dic_dataframe.csv")
