#2 columns, date and profit/loss

#produce:
#total number of months in the dataset
    #set month, if month is different increment, if month is different and blank increment and end
#net total Profits/Losses
    #add running total of all profit/loss cells as loop goes on
#average of the changes in profits/losses
    #create a list of each amount of change between profit/loss cells
    #run the sum of all that list, divided by the length of all that list for the average
#greatest increase in profits in date and amount
    #track the greatest profit/loss change and check it for an update on each cell of the list
#greatest decrease in loss in date and amount
    #track the lowest profit/loss change and check it for an update on each cell of the list



#set variables
#if cell = same, increment and continue
#if cell = different
    #if cell = blank
        #commit and end
    #else (if not blank)
        #commit and switch and reset monthlys while incrementing others


#
#import and set up
#

import os
import csv

TotalPL = 0
LastPL = 1666666666666666666667
PLChange = 0
Months = dict()  ## could be a list, really, if it's only one dimensional
greatest_profit = -50000000000
GP_date = ""
lowest_loss = 50000000000
LL_date = ""
change_list = list()
average_change = 0.00

NumofMonths = 0

#Specify the file path for the resource
bank_csv = os.path.join("Resources","budget_data.csv")

with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    cvs_header = next(csvfile)

    for row in csvreader:               
                     
        Month = row[0]
        if (Month in Months) :
            #Months[Month] += 1
            pass
            
        else:
            NumofMonths += 1
            Months.update({Month:0})

#   # increment to total P&L
        TotalPL = TotalPL + int(row[1])      ##adds the profit/loss record, so if it's negative it detracts from the total.
                                    ## triggers on all passes, first or otherwise

                                                    ################################################################################################
        if (LastPL != 1666666666666666666667) :     ##  This unlikely number is used as a specific start trigger to control the first pass case.  ##
            PLChange = int(row[1]) - LastPL              ################################################################################################
            
#   # add amount of change to average_list[]
            change_list.append(PLChange)


#   # check to replace greatest change (date and amount)
#   # check to replace lowest change (date and amount)
            if PLChange > greatest_profit :                         #######################################################################
                greatest_profit = PLChange                          ## This pair of If statements check for greatest and lowest change.  ##
                GP_date = row[0]                                    #######################################################################

            if PLChange < lowest_loss :
                lowest_loss = PLChange
                LL_date = row[0]


            LastPL = int(row[1])

        else:                           ##this else only triggers on the first pass, so is sort of an initializer

            if PLChange > greatest_profit :                         #######################################################################
                greatest_profit = PLChange                          ## This pair of If statements check for greatest and lowest change.  ##
                GP_date = row[0]                                    #######################################################################

            if PLChange < lowest_loss :
                lowest_loss = PLChange
                LL_date = row[0]
            LastPL = int(row[1])
    


#   # print and output txt file
    average_change = sum(change_list)/len(change_list)
    
    average_format = str(round(average_change, 2))

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(NumofMonths))
    print("Total: $" + str(TotalPL))
    print("Average Change: $" + str(average_format))
    print("Greatest Increase in Profits: " + str(GP_date) + " ($" + str(greatest_profit) + ")")
    print("Greatest Decrease in Profits: " + str(LL_date) + " ($" + str(lowest_loss) + ")")


    
    









