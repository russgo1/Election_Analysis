# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
'''
import datetime as dt
from inspect import FullArgSpec

print(dt.datetime.now())

import csv
###
# Assign a variable to the file to load and the path
file_to_load = "Resources/election_results.csv"

# Open and read
election_data = open(file_to_load, 'r')

# To do : perform analysis

# Close the file
election_data.close()
###
# Assign a variable to the file to load and the path
file_to_load = "Resources/election_results.csv"
# Open election results and read the file
with open(file_to_load) as election_data:

    # To do: Perform Analysis
    print(election_data)
###
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_anlysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some datat to the file. 
outfile.write("Hello World")

#Close the file
outfile.close()
'''
'''
# Import dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #Write soem data to the file.
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

with open(file_to_load) as election_data:

    #To do: read and analyze the data here. 
'''
# Updated through 3.5

'''
# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #Write soem data to the file.
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

# Initialize total votes variable
total_votes = 0
# Initialize candidate list
candidate_options = []
# Declare candidate-vote dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open and read CSV
with open(file_to_load) as election_data:

    #To do: read and analyze the data here. 
    
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # Increment vote counter
        total_votes += 1

        # Print the candidiate name from each row
        candidate_name = row[2]
        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add candidate to list of options
            candidate_options.append(candidate_name)

            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Iterate through list of candidates
for candidate_name in candidate_options:
    # Retrieve the vote count of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of the votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name and percentage of votes
    # print(f'{candidate_name} recived {vote_percentage:.1f}% of the vote.')

    # Print each candidate's name, vote count, and percentage of votes
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

    # Determine winning vote count and candidate
    # Determine if the votes are greater than the wining count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Set winning_candidate equal to candidate's name
        winning_candidate = candidate_name
    
# Print our the winning candidate, vote count, and percentage to terminal
winning_candidate_summary = (
    f'--------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'--------------------\n')
print(winning_candidate_summary)   


# Print the candidate vote dictionary
print(candidate_votes)

# Print the candidate list.
print(candidate_options)

# Print the total votes
print(total_votes)
'''    
  
