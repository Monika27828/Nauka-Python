import csv

with open('dane_telco.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)