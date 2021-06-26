import os
import csv

total_months = 0

#Create and define csvpath
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #Read the header row first
    csv_header = next(csvreader)

    #Read each row of data after the header
    total_months = sum(1 for total_months in csvreader)
    print("Total months: " + str(total_months))