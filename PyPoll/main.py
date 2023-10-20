import csv
import os
csvpath = os.path.join("." , "Resources", "election_data.csv")
with open(csvpath, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ",")
    row_count = 0
    CCS_count = 0
    DD_count = 0
    RAD_count = 0
    next(csv_reader)
    for row in csv_reader :
        count = row_count + 1
        row_count = count
        vote_count = row_count
        if row[2] == "Charles Casper Stockham":
            CCS_count = CCS_count + 1
        elif row[2] == "Diana DeGette":
            DD_count = DD_count + 1
        elif row[2] == "Raymon Anthony Doane":
            RAD_count = RAD_count + 1
CCS_percentage = (CCS_count/row_count)*100
DD_percentage = (DD_count/row_count)*100
RAD_percentage = (RAD_count/row_count)*100
print(CCS_percentage)
