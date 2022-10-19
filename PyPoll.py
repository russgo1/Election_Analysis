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

# Print the candidate vote dictionary
print(candidate_votes)

# Print the candidate list.
print(candidate_options)

# Print the total votes
print(total_votes)
    