#import xlrd
#import pandas as pd
import csv

lst = []
dicts = {}
# opening the CSV file
with open('Chevron Technical Skill Assessment Form (Responses).csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        lst.append(lines)
    for i in range(len(lst)):
        dicts[i] = lst[i]
    print(dicts)