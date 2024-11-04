import pandas as pd

# Files to load and output
load_file = "/Users/ugurcetin/Documents/Bootcamp_Data_Analyst/Github_HW/data_week3/03-Python/Starter_Code/PyPoll/Resources/election_data.csv"
output_file = "/Users/ugurcetin/Documents/Bootcamp_Data_Analyst/Github_HW/data_week3/03-Python/Starter_Code/PyPoll/analysis/Election_Results.txt"

# Load the election data
df = pd.read_csv(load_file)


# Calculate total votes
total_votes = len(df)

# Calculate vote counts and percentages for each candidate
vote_counts = df['Candidate'].value_counts()
vote_percentages = (vote_counts / total_votes) * 100

# Find the winner
winner = vote_counts.idxmax()

# Prepare the output lines
output_lines = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]
for candidate, votes in vote_counts.items():
    percentage = vote_percentages[candidate]
    output_lines.append(f"{candidate}: {percentage:.3f}% ({votes})")
output_lines.append("-------------------------")
output_lines.append(f"Winner: {winner}")
output_lines.append("-------------------------")

# Display results on the console
for line in output_lines:
    print(line)

# Write results to a text file
with open(output_file, 'w') as file:
    for line in output_lines:
        file.write(line + '\n')
