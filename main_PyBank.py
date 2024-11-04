# Dependencies
import os
import csv
 
# Files to load and output
load_file = "/Users/ugurcetin/Documents/Bootcamp_Data_Analyst/Github_HW/data_week3/03-Python/Starter_Code/PyBank/Resources/budget_data.csv" 
output_file = "/Users/ugurcetin/Documents/Bootcamp_Data_Analyst/Github_HW/data_week3/03-Python/Starter_Code/PyBank/analysis/financial_analysis.txt"
 
# Track various metrics
total_months = 0
net_amount = 0
previous_amount = 0
change_list = []
date_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]
 
# Read the csv and convert it into a list of dictionaries
with open(load_file) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
 
    # Get first row
    first_row = next(reader)
    total_months += 1
    net_amount += int(first_row[1])
    previous_amount = int(first_row[1])
 
    # Loop through rows
    for row in reader:
        # Track the total
        total_months += 1
        net_amount += int(row[1])
 
        # Track the change
        change = int(row[1]) - previous_amount
        change_list.append(change)
        date_list.append(row[0])
        previous_amount = int(row[1])
 
        # Calculate the greatest increase
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
 
        # Calculate the greatest decrease
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change
 
# Calculate the average change
average_change = sum(change_list) / len(change_list)
 
# Generate output summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_amount:,.2f}\n"
    f"Average Change: ${average_change:,.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]:,.2f})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]:,.2f})\n"
)
 
# Print output to terminal
print(output)
 
# Export results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)