import os
import csv
#Defining path for output file and csv file
csvpath = os.path.join(".", "Resources", "budget_data.csv")
output_path = os.path.join(".", "Analysis", "output.txt")
#Reading csv file
with open(csvpath, encoding='UTF-8') as csvfile :
    csvreader = csv.reader(csvfile, delimiter=",")
    #Declaring variable values
    row_count = 0
    sum = 0
    previous = 0
    Total_change = 0
    max_increase = 0
    max_decrease = 0
    next(csvreader)
    #Calculations
    for row in csvreader:
        row_count = row_count + 1
        Months_count = row_count
        sum = int(row[1]) + sum
        Total_profit_loss = sum
        current_profit_loss = int(row[1])
        change_profit_loss = current_profit_loss - previous
        Total_change = change_profit_loss + Total_change
        previous = current_profit_loss
        if change_profit_loss > max_increase:
            max_increase = int(change_profit_loss)
            max_increase_date = row[0]
        if change_profit_loss < max_decrease:
            max_decrease = int(change_profit_loss)
            max_decrease_date = row[0]
    Average_change = int(Total_change/(Months_count-1))
    #writing outputs to text file
    results = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Months_count}\n"
    f"Average Change: {Average_change}\n"
    f"Greatest Increase in Profits: {max_increase_date} ${max_increase}\n"
    f"Greatest Decrease in Profits: {max_decrease_date} ${max_decrease}\n"
    )
    with open(output_path,'w') as outputfile:
       outputfile.write(results)
   
    