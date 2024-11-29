# import csv

# with open("weather_data.csv") as data_file:
#     data=data_file.readline()
#     print(data)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])