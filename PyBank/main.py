import os
import csv

total_months = 0
profit_loss = []
net_total = 0
running_delta = []
running_delta_total = 0

#Create and define csvpath
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Read csv file
with open(csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')

    csv_header = next(budget_data)

    for row in budget_data:
	    profit_loss.append(row[1])
    
for net in range(len(profit_loss)):
    total_months = len(profit_loss)
    net_total = net_total +(int(profit_loss[net]))

for net in range(len(profit_loss)-1):
    running_delta.append((int(profit_loss[net+1])) - (int(profit_loss[net])))
    running_delta_total = running_delta_total +(int(running_delta[net]))
    avg_delta = running_delta_total/(len(running_delta))
print("Total months: " + total_months)
print("Total: " + net_total)
print(profit_loss)
print(running_delta_total)
print("Average Change: " + avg_delta)