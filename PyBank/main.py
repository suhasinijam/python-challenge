import os
import csv
csvpath = os.path.join(".", "Resources", "budget_data.csv")
with open(csvpath, encoding='UTF-8') as csvfile :
    csvreader = csv.reader(csvfile, delimiter=",")
    row_count = 0
    Total = 0
    next(csvreader)
    for row in csvreader:
        row_count = row_count + 1
        Months_count = row_count
        Total = int(row[1]) + Total
        Total_profit_loss = Total
    print(f'Total months {Months_count}')
    print(f'Total : ${Total_profit_loss}')
   
    