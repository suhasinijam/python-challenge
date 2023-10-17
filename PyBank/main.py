import os
import csv
csvpath = os.path.join("..", "Resources", "budget_data.csv")
with open(csvpath, encoding='UTF-8') as csvfile :
    csvreader = csv.reader(csvfile, delimiter=",")
    row_count = 0
    for row in csvreader:
        row_count += 1
        print(row)
   
    