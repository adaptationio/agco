import numpy as np


import csv

with open('dataold/Locations.csv', newline='') as csvfile:
    locations = list(csv.reader(csvfile))

with open('dataold/Systems.csv', newline='') as csvfile:
    systems = list(csv.reader(csvfile))


print(locations[0])
print(systems[0])
print(locations[1])
print(systems[1])

import csv
 
def readMyFile(filename):
    dates = []
    scores = []
 
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            dates.append(row[0])
            scores.append(row[1])
 
    return dates, scores
 
 
dates,scores = readMyFile('dataold/Systems_with_user_address_council.csv')
 
print(dates)
print(scores)