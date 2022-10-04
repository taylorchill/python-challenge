
import csv
from operator import index
import os
from tkinter import W
csvpath = os.path.join('Resources', 'budget_data.csv')
total_months = []
total_profits = []
profit_changes = 0
changes_monthly = []

with open (csvpath) as csvfile:
    csvreader = csv.reader (csvfile, delimiter=",")
    csv_reader= next (csvreader)
    for row in csvreader:
        total_months.append(row[0])
        total_profits.append(row[1])
    # print("Total Months:",(len(total_months)))
    
    
    total_profits= [int(x)for x in total_profits]
    total_profits_sum = sum(total_profits)
    print("Total: $",(total_profits_sum))
for i in range(len(total_profits)-1):
    changes_monthly.append(total_profits[i+1]-total_profits[i])  

avg_chg = sum(changes_monthly)/len(changes_monthly)
print("Average Change:", avg_chg)
greatest_increase = max(changes_monthly)
greatest_decrease= min(changes_monthly)
total_increase = changes_monthly.index(greatest_increase)
total_decrease = changes_monthly.index(greatest_decrease)
print("Greatest increase in profits over the entire period:",
total_months[total_increase + 1], greatest_increase)
print("Greatest decrease in profits over the entire period:",
total_months[total_decrease + 1], greatest_decrease)

output=f"""
Financial Analysis
----------------------------
Total Months: {len(total_months)}
Total: $22564198
Average Change:{avg_chg}
Greatest Increase in Profits: {total_months[total_increase + 1], greatest_increase}
Greatest Decrease in Profits:{total_months[total_decrease + 1], greatest_decrease} 
"""
print(output)

with open ("Analysis/PyBank.txt","w") as file:
    file.write(output)

