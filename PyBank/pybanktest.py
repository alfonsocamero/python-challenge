import os
import csv

total_months = 0
profit_loss = []
net_total = 0
avg_delta = []

#Create and define csvpath
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Read csv file
with open(csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')

    csv_header = next(budget_data)

    for row in budget_data:
	    profit_loss.append(row[1])
    #print(profit_loss)

for net in range(len(profit_loss)):
    total_months = len(profit_loss)
    net_total = net_total +(int(profit_loss[net]))
    avg_delta.append((int(profit_loss[net])) - (int(profit_loss[net-1])))
print(total_months)
print(net_total)
print(avg_delta[net - 1])