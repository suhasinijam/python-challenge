import os
import csv
#Defining path
csvpath = os.path.join(".", "Resources", "election_data.csv")
output_path = os.path.join(".", "Analysis", "output.txt")
#Declaring values
vote_count = 0
CCS_count = 0
DD_count = 0
RAD_count = 0
#Opening CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    #Into loops for calculations
    for row in csv_reader:
        vote_count = vote_count + 1    
        candidate = row[2]
        if candidate == "Charles Casper Stockham":
            CCS_count = CCS_count + 1
        elif candidate == "Diana DeGette":
            DD_count = DD_count + 1
        elif candidate == "Raymon Anthony Doane":
            RAD_count = RAD_count + 1
CCS_percentage = float((CCS_count / vote_count) * 100)
DD_percentage = float((DD_count / vote_count) * 100)
RAD_percentage = float((RAD_count / vote_count) * 100)
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
vote_counts = [CCS_count, DD_count, RAD_count]
winner = candidates[vote_counts.index(max(vote_counts))]
#writing outputs to text file
results = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {vote_count}\n"
    f"Charles Casper Stockham: {CCS_percentage:.3f}% ({CCS_count})\n"
    f"Diana DeGette: {DD_percentage:.3f}% ({DD_count})\n"
    f"Raymon Anthony Doane: {RAD_percentage:.3f}% ({RAD_count})\n"
    f"Winner: {winner}\n"
    )
with open(output_path,'w') as outputfile:
    outputfile.write(results)