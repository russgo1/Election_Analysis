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
    
