# With file
with open("weather_data.csv") as data_file:
    data = data_file.readlines()

print(data)

# With csv
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# With pandas
import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data)) #dataframe (whole table)
# print(type(data["temp"])) #series (column)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()

# Calculating the mean Python list
mean_temp = sum(temp_list) / len(temp_list)
print(mean_temp)

# Calculating the mean pandas descriptive stats
print(data["temp"].mean())

# Get the max temperature
print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)

# Get Data in row
print(data[data.day == "Monday"])

# Get day with max temperature
print(data[data.temp == data.temp.max()])

# Particular row value
monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from dictionary
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

scores_data = pandas.DataFrame(data_dict)
scores_data.to_csv("scores_data.csv")