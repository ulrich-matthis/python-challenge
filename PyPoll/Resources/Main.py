
#Create list of dependencies
import os 
import csv

#Create a variable to load our file from path
election_data = os.path.join("..", "Resources", "election_data.csv")

save_file = os.path.join("..","analysis", "election_results.txt")

#Created a vote counter
Vote_Count = 0

#Created variables to store our candidates and their vote counts
Candidate_Selection = []
Candidate_Votes = {}
Candidate_Votes_Total = []

#Tracker for displaying winning candidate
Win_Candidate = ""
Win_Count = 0
Win_Percentage = 0

#CSV file opened and corresponding columns converted into lists for analysis
with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ",")

#Header row stored
    csv_header = next(csv_reader)


    for row in csv_reader:
        
        Vote_Count += 1

        Candidate = row[2]

#Counting the overall vote total while creating a list of candidates within data set


        if Candidate not in Candidate_Selection:
            Candidate_Selection.append(Candidate)
        
            Candidate_Votes[Candidate] = 0

        Candidate_Votes[Candidate] +=1

#Printing Total number of votes/rows regardless of candidate selection
        election_result = (
            f"\nElection Results\n"
            f"----------------------------\n"
            f"Total Votes: {Vote_Count:}\n"
            f"----------------------------\n"
        )
#Result printed to terminal
print(election_result)

#Loop to tabulate vote count for each respective candidate with the CSV File
for Candidate in Candidate_Votes:

        votes = Candidate_Votes.get(Candidate)

        vote_percent = float(votes) / float(Vote_Count) * 100

        candidate_result = f"{Candidate}: {vote_percent:.3f}% ({votes:})\n"

        Candidate_Votes_Total.append(candidate_result)
#Printed result list for each candidate within the terminal
        print(candidate_result)

#Determine winner of the election
        if (votes > Win_Count) and (vote_percent > Win_Percentage):
            Win_Candidate = Candidate
            Win_Count = votes
            Win_Percentage = vote_percent
#Print results to the terminal
election_summary = (
        f"-------------------------------\n"
        f" \n"
        f"Winner: {Win_Candidate}\n"
        f" \n"
        f"--------------------------------\n"
    )

print(election_summary)

#Export results to corresponding folder
with open(save_file, "w") as txt_file:
    txt_file.write(election_result)
    txt_file.write(str(Candidate_Votes_Total[0]))
    txt_file.write(str(Candidate_Votes_Total[1]))
    txt_file.write(str(Candidate_Votes_Total[2]))
    txt_file.write(election_summary)