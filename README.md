# Election Audit Analysis

## Overview

The purpose of this audit is to determine election results by candidate and by county. It determines the vote count and percentage of the total vote for each candidate and each county. It also determined the winning candidate and the county with the largest voter turnout. 

## Results

#### All of the analysis referenced here was done based on the contents of the “election_results.csv” file located in the “Resources” folder. Each bullet point is followed by a screenshot of the relevant annotated code. 

- In total, **369,711 votes were cast in this election**. The following code was used to determine this.
[INSERT PIC]

- Three counties participated in this election. **Jefferson County** had **38,855 voters**, making **10.5%** of the total voter turnout. **Denver County** had **306,055 voters**, making **82.8%** of the turnout. Finally, **Arapahoe County** turned out **24,801 voters**, making **6.7%** of the total.
[INSERT PIC]

- Denver County had the largest number of votes.
[INSERT PIC]

- Three candidates participated in this election. **Charles Casper Stockham** received **23.0% of the vote** with **85,213** total votes. **Diana DeGette** received **73.8% of the vote** with **272,892** total votes. Finally, **Raymon Anthony Doane** received **3.1% of the vote** with **11,606** total votes.
[INSERT PIC]

- The winner of the election was **Diana DeGette** with **272,892 total votes**, making **73.8%** of the total.
[INSERT PIC]

## Summary

This script is written in a clean versatile way that makes it an excellent choice for use in future elections. The script relies on the placement of information in a CSV file, rather than the text itself, which makes it versatile. For example, in an another election where precincts (not counties) are used to group voters, one would only want to modify the script slightly to change “county” in variable names and text output to “precinct” for clarity. From there, one would only need to ensure that the proper fields are referenced from the CSV file, and the script will do the rest. 

This script will work equally as well for any number of candidates or voting precincts. Let’s say, for instance, that this script were needed for a gubernatorial race where voters were voting for not one, but two candidates (governor and lieutenant governor). This script could easily be modified to include an output that lists lieutenant governor along with the governor. A new dictionary could be created to pair governor keys with lieutenant governor values, the same way candidate names are currently paired with vote counts. It might look something like `{candinate_name: ltn_gov_name}`. Then we could print or write the lieutenant governor’s name by referencing the corresponding gubernatorial candidate’s name. 
