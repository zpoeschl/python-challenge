# Import CSV

import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Lists to store CSV data
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

    # Calculate number of votes cast
    total_votes = len(voter_id)

    print(f'Total votes: {total_votes}')

    # Identify and print unique candidate names and store in a list
    unique_candidate = []
    def unique(candidate):

        for name in candidate:
            if name not in unique_candidate:
                unique_candidate.append(name)
        
        for name in unique_candidate:
            return name

    unique(candidate)

    # Calculate total number of votes each candidate won and store in a list
    votes_per_candidate = []
    def count_votes(unique_candidate):

        # set initial count
        vote_total = 0

        for name in unique_candidate:
            for vote in candidate:
                if name == vote:
                    vote_total = int(vote_total) + 1
                
            votes_per_candidate.append(vote_total)

            # reset count
            vote_total = 0

        return votes_per_candidate

    count_votes(candidate)

    # Calculate percentage of votes each candidate won and store in a list
    vote_percentage = []

    for x in (votes_per_candidate):
        percentage = round((float(int(x) / int(total_votes)) * 100), 3)

        vote_percentage.append(percentage)

    combined_results = tuple(zip(unique_candidate, votes_per_candidate, vote_percentage))
    
    # Determine the election winner
    winner = max(votes_per_candidate)

# print results in terminal
print(f'Total votes: {total_votes}')
for lst in combined_results:
    print(f'{lst[0]}: {lst[1]}00% {lst[2]}')
print(f'Winner: {winner}')

# export to text file
output_path = os.path.join('Analysis', 'PyPoll.txt')

with open(output_path, 'w') as text:

    print(f'Total votes: {total_votes}', file = text)
    for lst in combined_results:
        print(f'{lst[0]}: {lst[1]}00% {lst[2]}', file = text)
    print(f'Winner: {winner}', file = text)