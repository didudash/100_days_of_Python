import csv
import pandas
from functools import reduce

# Exploration of csv files


def Average(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)


data_1 = []
with open("weather_data.csv") as file:
    for line in file:
        data_1.append(line.strip())
    print(f"Every line as an item of a list {data_1}")

temperatures = []
with open("weather_data.csv") as file:
    data_2 = csv.reader(file)
    i = 0
    for row in data_2:
        if i > 0:
            temperatures.append(int(row[1]))
        i += 1
print(f"Temperatures of the csv file {temperatures}")

data_3 = pandas.read_csv("weather_data.csv")

print(type(data_3))
print(type(data_3["temp"]))

data_dict = data_3.to_dict()
print(data_dict)

temp_list = data_3["temp"]
print(len(temp_list))
avg_temp = Average(temp_list)
print(avg_temp)
print(data_3["temp"].mean())

print(data_3["temp"].max())

print("Weather conditions", data_3.condition)

# Get data in a row
print(data_3[data_3.temp == data_3.temp.max()])

# Monday's temperatur in Fahrenheit
print(
    f"Monday's temperatur in Fahrenheit {int(data_3.temp[data_3.day == 'Monday'])*9/5 + 32}"
)

# Create DataFrame from scratch
data_dict_4 = {"students": ["Amy", "James"], "scores": [76, 56]}
data_4 = pandas.DataFrame(data_dict_4)
