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
