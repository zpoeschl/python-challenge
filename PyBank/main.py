# Modules

import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
months = []
profit_losses = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)

    # Move CSV data into lists and treat profit/losses as number(integer)
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

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

    # Calculate number of months
    month_count = len(months)

    # Calculate net total of Profit/Losses
    net_total = sum(profit_losses)

    # Calculate changes in Profit/Losses
    total_change = 0

        # Calculate average change
    average_change = 0

    # Calculate greatest increase in profits
    greatest_increase = max(profit_losses)

    # Calculate greatest decrease in profits  
    greatest_decrease = min(profit_losses)

    # Print number of months
    print(f'Total number of months: {month_count}')

    # Print net total of Profit/Losses
    print(f'Net total of Profit/Losses: {net_total}')

    # Print average change in Profit/Losses
    print(f'Average change: {average_change}')

    # Print greatest increase in profits
    print(f'Greatest increase in profits: {greatest_increase}')

    # Print greatest decrease in profits
    print(f'Greatest decrease in profits: {greatest_decrease}')