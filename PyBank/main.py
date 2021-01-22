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

    # Calculate number of months
    month_count = len(months)

    # Calculate net total of Profit/Losses
    net_total = sum(profit_losses)

    # Calculate changes in Profit/Losses
    total_change = 0

    for 





        # Calculate average change
    average_change = mean(total_change)

    # Calculate greatest increase in profits
    greatest_increase = max(total_change)

    # Calculate greatest decrease in profits  
    greatest_decrease = min(total_change)

    # Print results to terminal
    print(f'Total number of months: {month_count}')
    print(f'Net total of Profit/Losses: {net_total}')
    print(f'Average change: {average_change}')
    print(f'Greatest increase in profits: {greatest_increase}')
    print(f'Greatest decrease in profits: {greatest_decrease}')

# export results to text file
output_path = os.path.join("Analysis", "PyBank.txt")

with open(output_path, 'w') as text:

    print(f'Total number of months: {month_count}', file = text)
    print(f'Net total of Profit/Losses: {net_total}', file = text)
    print(f'Average change: {average_change}', file = text)
    print(f'Greatest increase in profits: {greatest_increase}', file = text)
    print(f'Greatest decrease in profits: {greatest_decrease}', file = text)