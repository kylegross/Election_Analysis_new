# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

In completing the above taks, the votes for the Colorado Board of Elections was analyzed to determine the winning candidate and the county with the largest voter turnout.

## Resources
- Data source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code 1.38.1

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The votes counted were from three different counties. As evident in the below vote counts per county, Denver by far had the largest number of votes.
    - Jefferson (received 10.5% of the vote and 38,855 total votes)
    - Denver (received 82.8% of the vote and 306,055 total votes)
    - Arapahoe (received 6.7% of the vote and 24,801 total votes)
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
 - The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 total votes.
    - Diana DeGette received 73.8% of the vote and 272,892 total votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes.
 - The winner of the election was:
    - Candidate Diana DeGette, who received 73.8% of the vote and 272,892 total votes
 
 The below screenshot provides a summary of all of the results:
 
 ![election_txt_image](https://github.com/kylegross/election-analysis/blob/master/election_txt_image.JPG)

## Challenge Summary
The code used in this analysis could be resused for other elections around the country, not just for a few counties within a single state. Modifications will need to be done in the case of reformatting election data to fit the model, for example changing the file type to a csv. That said, there are different python packages available that are best suited to other file types. In addition, the general structure of the code should be similar across all documents, as the data for election results will all contain a list of candidates, counties, and number of votes. This means that the winning candidate and the highest voter turnout per county could still be calculated is written once the file is properly converted. In terms of a national election, the data structure will need to be reformated to account for different territory levels within the fifty states. For example, it would be important to show not only county votes, but also the total votes per state and whether the state/county is predominately democratic or republican. Depending on how the data is sorted, the code must be revised to account for changes in column names and the general data organization.
