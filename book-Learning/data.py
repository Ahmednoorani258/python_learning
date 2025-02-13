# import the csv module
import csv

# open the csv file
with open('nfl_offensive_stats.csv', 'r') as file:
    # create a csv reader object
    data = list(csv.reader(file))

passing_yards ={}

for row in data:
    if row[2] == 'QB' :
        if row[3] in passing_yards :
            passing_yards[row[3]] += int(row[7])
        else :
            passing_yards[row[3]] = int(row[7])   


passing_yards.pop('Tom Brady')

# only print top 5
for key, value in sorted(passing_yards.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(key, value)