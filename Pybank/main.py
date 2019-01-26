#Goals to Calculate for Pybank

#1 The total number of months included in the dataset

#2 The total net amount of "Profit/Losses" over the entire period

#3 The average change in "Profit/Losses" between months over the entire period

#4  The greatest increase in profits (date and amount) over the entire period

#5 The greatest decrease in losses (date and amount) over the entire period



#Step 1 Load Dependencies:

import csv
import os

# Step 2 Load the files

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Output_Analysis", "final_analysis.txt")

# Create Variables to track Financials

allmonths = 0
monthschange = []
netchange = []
biggestincrease = ["", 0]
biggestdecrease = ["", 9999999999999999999]
totalnetchange = 0

# Load CSV and Create Dictionaries


with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to netchange
    first_row = next(reader)
    allmonths = allmonths + 1
    totalnetchange = totalnetchange + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total
        allmonths = allmonths + 1
        totalnetchange = totalnetchange + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        netchange = netchange + [net_change]
        monthschange = monthschange + [row[0]]

        # Calculate the greatest increase
        if net_change > biggestincrease[1]:
            biggestincrease[0] = row[0]
            biggestincrease[1] = net_change

        # Calculate the greatest decrease
        if net_change < biggestdecrease[1]:
            biggestdecrease[0] = row[0]
            biggestdecrease[1] = net_change

# Funtion to Calculate Average Net Change

totalmonthlyavg = sum(netchange) / len(netchange)

#Print out the results in Text File

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)