import csv
with open("D:/20mca015/New.csv", "r",) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)