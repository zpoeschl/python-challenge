# Import CSV

import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Lists to store data
voter_id = []
county = []
candidate = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)

    # Move CSV data into lists
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# -----------------------------------------------------------------------
# INSTRUCTIONS
# Analyze the following:
#       The total number of votes cast
#       A complete list of candidates who received votes
#       The percentage of votes each candidate won
#       The total number of votes each candidate won
#       The winner of the election based on popular vote
#
# Final script should both print the analysis to the terminal and export a text file with the results
#
# -----------------------------------------------------------------------

    # Calculate number of votes cast
    total_votes = len(voter_id)

    print(f'Total votes: {total_votes}')

    # Identify and print unique candidate names
    def unique(candidate):
        unique_candidate = []

        for name in candidate:
            if name not in unique_candidate:
                unique_candidate.append(name)
        
        for name in unique_candidate:
            print(name)
            #print(f'{name}: {percent_vote} 'f'({total_votes})')

    unique(candidate)