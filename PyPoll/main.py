import os
import csv

all_votes = []
candidate_list = []
total_votes = 0
name1_count = 0
name2_count = 0
name3_count = 0
name4_count = 0

#Create and define csvpath
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#Read csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csv_reader)

    for col in csv_reader:
        all_votes.append(col[2])
        total_votes = len(all_votes)

for name in range(len(all_votes)):
    if all_votes[name] not in candidate_list:
        candidate_list.append(all_votes[name])
name1 = candidate_list[0]
name2 = candidate_list[1]
name3 = candidate_list[2]
name4 = candidate_list[3]

for count in range(len(all_votes)):
    if name1 == all_votes[count]:
        name1_count = name1_count + 1
    if name2 == all_votes[count]:
        name2_count = name2_count + 1

print("Election Results")
print("Total Votes: " + str(total_votes))
print(str(name1) + ": " + str(name1_count))
print(str(name2) + ": " + str(name2_count))