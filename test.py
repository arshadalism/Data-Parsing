import csv

with open('merged_data.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for data in reader:
        print(data)