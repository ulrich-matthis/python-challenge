
#Create list of dependencies
import os
import csv

#Create variable and load file from pathway
budget_data = os.path.join("..","Resources", "budget_data.csv")

save_file = os.path.join("..", "analysis", "budget_analysis.txt")

#Month Counter
Months = 0

#Total Financials Column Counter
Financials_Total = 0

#Variable for tracking monthly change
Value = 0

#Counter to analyze change month to month
Change = 0

#List to record all dates in the set
Date = []

#List to record all Financial values within the set
Financials = []

#Open and read the CSV File
with open(budget_data, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ",")

#Record the header row
    csv_header = next(csv_reader)

#Begin counting with the first row after the header row
    heading = next(csv_reader)

#Count months
    Months += 1

#Add the values in column 1 to financial total
    Financials_Total += int(heading[1])
    Value = int(heading[1])

#Analyze monthly change and append the value to the respective month
    for row in csv_reader:

        Date.append(row[0])

        Change = int(row[1])-Value
        Financials.append(Change)
        Value = int(row[1])

        Months += 1

        Financials_Total = Financials_Total + Value

#Determine the average change in Financials across the entire data set
Financial_Avg = sum(Financials)/len(Financials)

#Determine which month had the greatest increase profits
Financial_Greatest_Increase = max(Financials)
Index_Greatest_Increase = Financials.index(Financial_Greatest_Increase)
Month_Greatest_Increase = Date[Index_Greatest_Increase]

#Determine which month had the greatest decrease in profits    
Financial_Greatest_Decrease = min(Financials)
Index_Greatest_Decrease = Financials.index(Financial_Greatest_Decrease)
Month_Greatest_Decrease = Date[Index_Greatest_Decrease]

#Print results from script
printfinalresult = (
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {str(Months)}\n"
    f"Total: ${(Financials_Total)}\n"
    f"Average Change: ${(round(Financial_Avg, 2))}\n"
    f"Greatest Increase in Profits: {Month_Greatest_Increase} (${str(Financial_Greatest_Increase)})\n"
    f"Greatest Decrease in Profits: {Month_Greatest_Decrease} (${str(Financial_Greatest_Decrease)})\n")
print(printfinalresult)

with open(save_file, "w") as txt_file:
    txt_file.write(printfinalresult)