# Import CSV

import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

# -----------------------------------------------------------------------
# INSTRUCTIONS
# Calculate the following:
#       The total number of months included in the dataset
#       The net total amount of "Profit/Losses" over the entire period
#       The changes in "Profit/Losses" over the entire period
#               Then find the average of those changes
#       The greatest increase in profits (date and amount) over the entire period
#       The greatest decrease in losses (date and amount) over the entire period
#
# Final script should both print the analysis to the terminal and export a text file with the results
#
# -----------------------------------------------------------------------

