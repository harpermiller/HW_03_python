#PyPoll

import os
import csv
from collections import Counter

newfile = os.path.join('PyPoll_Results.txt') #Path of the results text file

with open("election_data.csv", "r") as csvfile: #Open and Read the csv
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    #Create empty lists
    candidate_votes_count = Counter()
    candidates_list = []
    percentage_list = []
    election_results = []

    for row in csvreader: #Print count of votes
        candidates_list.append(row[2]) #Add candidate names to list

    total_votes = len(candidates_list) #Total votes is the length of candidates_list

    for name in candidates_list:
        candidate_votes_count[name] += 1 #Aggregates duplicates

    #Finds the candidate with the highest vote count and labels them the winner
    election_winner = max(zip(candidate_votes_count.values(), candidate_votes_count.keys())) #Finds the candidate with the highest vote count and labels them the winner
    candidate_names = tuple(candidate_votes_count.keys()) #Creates tuple called candidate_names that stores the names of the candidates
    votes = tuple(candidate_votes_count.values()) #Creates tuple called votes that stores the amounts of votes

    for vote in votes:
        percentage_list.append((int(vote) / total_votes) * 100)

    #Add elements to election_results list for final output
    election_results.append("Election_Results")
    election_results.append("=======================")
    election_results.append(f"Total Votes: {total_votes}")
    election_results.append("=======================")


    for n in range(len(candidate_names)): #Listing final candidate data
        election_results.append(f"{candidate_names[n]}: {round(percentage_list[n],2)}% {votes[n]}")

    election_results.append("=======================")
    election_results.append(f"The winner is: {election_winner[1]}")
    election_results.append("=======================")

    print("\n".join((election_results))) #Print election results

with open(newfile, 'w') as txtfile: #Write text file with results
    txtfile.write('\n'.join(election_results))
