##############################################
##  Main.py - PyPoll project - Bill Riggio  ##
##############################################

import os
import csv

#Specify the file path for the resource
poll_csv = os.path.join("Resources","election_data.csv")

#Specify the file path for the output



#list of needed variables :
#
# TotalVotes amount, Candidates{} dictionary, with CandName : CandVotes, CandidateAmount for easy looping, HighestAmount & YoureWinner for final results

TotalVotes = 0
Candidates = dict()
count = 0
NumofCandidates = 0



with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    cvs_header = next(csvfile)
    #adjusts past the header row
  

    for row in csvreader:               #This loop parses through the whole content, with conditions for a new candidate or an existing candidate.
        TotalVotes = TotalVotes+1       #It then either adds the candidate to the dictionary above or not, and increments the vote either way for both
        Candidate = row[2]              #total vote as a separate variable or individual vote as part of the dictionary.

        if (Candidate in Candidates) :
            Candidates[Candidate] += 1
            
        else:
            NumofCandidates += 1
            Candidates.update({Candidate:0})
            Candidates[Candidate]+=1
    

    print("Election Results")                   ## Begin output of printing info
    print("-------------------------")
    print("Total Votes:" + str(TotalVotes))     ## Report total votes
    print("-------------------------")
    

    WhosWinner = 0                              #These set empty variables and easy conditions to surpass for the vote count
    YoureWinner = " "
    for cand in Candidates:
        percent = Candidates[cand] / TotalVotes
        percent_format = "{:.2%}".format(percent)
        print(cand + ": " + str(percent_format) + " (" + str(Candidates[cand]) + ")")
        if (Candidates[cand] > WhosWinner):
            WhosWinner = Candidates[cand]
            YoureWinner = cand

       
    print("-------------------------")
    print("Winner: " + YoureWinner)
    print("-------------------------")
   


 ## Last of all, the code creates and then writes to a text file.                                   
output_txt = open("output.txt", "w")
output_txt.write("Election Results\n")
output_txt.write("-------------------------\n")
output_txt.write("Total Votes:" + str(TotalVotes)+" \n")
output_txt.write("-------------------------\n")
for cand in Candidates:
        percent = Candidates[cand] / TotalVotes
        percent_format = "{:.2%}".format(percent)
        output_txt.write(cand + ": " + str(percent_format) + " (" + str(Candidates[cand]) + ")\n")

output_txt.write("-------------------------\n")
output_txt.write("Winner: " + YoureWinner +"\n")
output_txt.write("-------------------------\n")
output_txt.close()
