# data_week3
Data Bootcamp Week 3 - HW

Financial Analysis Script

A Python script to analyze financial data from a CSV file, calculating total months, net profit/loss, average monthly change, and the greatest increase and decrease in profits. The results are printed to the console and saved in a text file.

Requirements

Python 3.x
Setup

Update File Paths: Ensure the paths for load_file (input CSV) and output_file (output text file) are correct in the script.
Run the Script:
bash
Copy code
python /path/to/your_script.py
Output

The script generates an financial_analysis.txt file with results in the following format:

yaml
Copy code
Financial Analysis
----------------------------
Total Months: 86
Total: $38,382,578.00
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1,926,159.00)
Greatest Decrease in Profits: Sep-2013 ($-2,196,167.00)



Election Results Analysis

A Python script to analyze election data, calculating total votes, each candidate's percentage and vote count, and the winner. Results are printed to the console and saved in a text file.

Requirements

Python 3.x
pandas library
Setup

Install pandas:
bash
Copy code
pip install pandas
Run the Script: Update the paths for load_file and output_file in the script if needed, then execute:
bash
Copy code
python /path/to/main_poll.py
Output

The script generates Election_Results.txt with results formatted as follows:

markdown
Copy code
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
