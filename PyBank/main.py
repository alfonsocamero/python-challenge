import os
import csv

total_months = 0
profit_loss = []
dates_list = []
net_total = 0
running_delta = []
running_delta_total = 0

#Create and define csvpath
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Read csv file
with open(csvpath) as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')

    csv_header = next(budget_data)

    for col in budget_data:
        profit_loss.append(col[1])
        dates_list.append(col[0])
    
for net in range(len(profit_loss)):
    total_months = len(profit_loss)
    net_total = net_total +(int(profit_loss[net]))

for net in range(len(profit_loss)-1):
    running_delta.append((int(profit_loss[net+1])) - (int(profit_loss[net])))
    running_delta_total = running_delta_total +(int(running_delta[net]))
    avg_delta = running_delta_total/(len(running_delta))
    greatest_increase = max(running_delta)
    greatest_decrease = min(running_delta)
for index in range(len(running_delta)):
    if running_delta[index] == greatest_increase:
        greatest_increase_date = (index + 1)
    if running_delta[index] == greatest_decrease:
        greatest_decrease_date = (index + 1)

print("Total months: " + str(total_months))
print("Total: " + str(net_total))
print("Average Change: " + str(avg_delta))
print(str(dates_list[greatest_increase_date]) + " " + str(greatest_increase))
print(str(dates_list[greatest_decrease_date]) + " " + str(greatest_decrease))

output_path = os.path.join('..', 'PyBank', 'Analysis', 'budget_data_analysis.txt')

with open(output_path, "w") as text_file:

 # Write the Title
    text_file.write("Financial Analysis " + " " + "\n")

    # Write the second-sixth row
    text_file.write("Total months: " + str(total_months) + "\n")
    text_file.write("Total: " + str(net_total)+ "\n")
    text_file.write("Average Change: " + str(avg_delta)+ "\n")
    text_file.write(str(dates_list[greatest_increase_date]) + " " + str(greatest_increase) + "\n")
    text_file.write(str(dates_list[greatest_decrease_date]) + " " + str(greatest_decrease) + "\n")