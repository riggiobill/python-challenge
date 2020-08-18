#PyPoll Notes

# 3 columns, VoterID, County, Candidate
#total number of votes cast
    #add running tally through cells
# complete list of candidates
    #same as month list - check for new, if new add to list and reset for next
    #dictionary of candidates and votes?
    #new candidate -  add new votes for last same entry and add new entry to list
    #add votes to current candidate entry on list until loop changes

#  of votes of overall won for each candidate
# ----- connected with below : total number of votes / total votes from above = percent for individual
#       format as percent after passthrough
#total number of votes won for each candidate
#     the loop needs to keep track of volume of overall votes and amount of votes for each candidate. Then at the end of the looping it can determine:
#   A. Who got how many votes each
#   B. What those percentages were, and
#   C. Who won the popular vote
# 
# Last: winner of the election based on popular vote, from vote count above
# 

import os
import csv
