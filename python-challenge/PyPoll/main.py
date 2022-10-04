import csv
import os 
csvpath= os.path.join('Resources','election_data.csv')
total_votes= 0
candidates= dict ()
total_percentage = dict()
total= 0
Charles_votes = 0
Diana_votes = 0
Raymon_votes = 0 

with open (csvpath) as csvfile:
    csvreader = csv.reader (csvfile, delimiter=",")
    csv_reader= next (csvreader)
   
    for row in csvreader:
       
        total_votes +=1
        candidates_names= row[2]
        

        if row[2] == "Charles Casper Stockham":
            Charles_votes += 1
        elif row[2] == "Diana DeGette":
            Diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_votes += 1
        

Charles_percentage= Charles_votes/total_votes * 100
Diana_percentage = Diana_votes/total_votes * 100
Raymon_percentage= Raymon_votes/total_votes *100  

dict_candidates_and_votes = {
    "Raymon Anthony Doane": Raymon_votes,
    "Diana DeGette": Diana_votes,
    "Charles Casper Stockham": Charles_votes}
    
Winner_name= ""
Winner_votes=0   

for candidate, votes in dict_candidates_and_votes.items():
    if votes > Winner_votes:
        Winner_votes = votes
        Winner_name = candidate



output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: {Charles_percentage:.3f}% ({Charles_votes:,})
Diana DeGette: {Diana_percentage:.3f}% ({Diana_votes:,})
Raymon Anthony Doane: {Raymon_percentage:.3f}%  ({Raymon_votes:,})
-------------------------
Winner: {Winner_name}
-------------------------
"""
print(output)

with open ("Analysis/PyPoll.txt","w") as file:
    file.write(output)
