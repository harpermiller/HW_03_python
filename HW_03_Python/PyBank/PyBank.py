#PyBank

import os
import csv
from statistics import mean

newfile = os.path.join('PyBank_Analysis.txt') #Path of the results text file

with open("budget_data.csv", "r") as csvfile: #Open and Read the csv
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader) #Now we can read the file without the header

    profit = [] #List of values in 2nd column
    monthly_change = []
    month_year = []
    financial_analysis = [] #Final output list

    for row in csvreader: #loop through each row
        profit.append(int(row[1])) #add profit/loss to the profit list

        total_profit = sum(profit) #Sum of elements in profit
        total_months = len(profit) #The total amount of months is the length of profit_loss

    for i in range(1, len(profit)): #Loop
        monthly_change.append(profit[i] - profit[i - 1]) #
        average_change = round(mean(monthly_change), 2) #

        max_difference = max(monthly_change) #define max_difference
        min_difference = min(monthly_change) #define min_difference

        month_year.append(row[0]) 
        max_difference_date = str(month_year[monthly_change.index(max(monthly_change))]) #Define the max_difference
        min_difference_date = str(month_year[monthly_change.index(min(monthly_change))]) #Define the min_difference

    financial_analysis.append("Financial Analysis")
    financial_analysis.append("=================================================")
    financial_analysis.append(f"Total Months: {total_months}")
    financial_analysis.append(f"Total: ${total_profit}")
    financial_analysis.append(f"Average Change: ${average_change}")
    financial_analysis.append(f"Greatest Increase in Profits: {max_difference_date}: ${max_difference}")
    financial_analysis.append(f"Greatest Decrease in Profits: {min_difference_date}: ${min_difference}")
    financial_analysis.append("=================================================")
    print("\n".join(financial_analysis))

with open(newfile, 'w') as txtfile: #Write text file with results
    txtfile.write('\n'.join(financial_analysis))
