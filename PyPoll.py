# CONNECT TO THE FILE AND LOAD ELECTION RESULTS
# Add our dependencies
import csv
import os
# Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to load a file from a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# READ AND ANALYZE THE DATA
# Open the election results and read the file
with open(file_to_load) as election_data:   
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Print the header row
    headers = next(file_reader)
    print(headers)


# ELECTION DATA ANALYSIS
# The data we need to retreive:
    # 1. Total number of votes cast
    # 2. Complete list of candidates who received votes
    # 3. Total number of votes per candidate
    # 4. Percentage of votes each candidate won
    # 5. The winner of the election based on popular vote


# Using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:
    # Write thee counties to the file
    #txt_file.write("COUNTIES IN THE ELECTION\n-------------------------\nArapahoe\nDenver\nJefferson")