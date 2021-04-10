import os
import csv


# input and ouptut files
ifile = "03-Python_hw_Instructions_PyBank_Resources_budget_data.csv"
ofile = "PyBank.txt"


# variables
total_months = 0
month_of_change = []
revenue_change_list = []
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""
total_revenue = 0


#opening and reading csv
with open(ifile, encoding='utf-8') as inputfile: 
	reader = csv.DictReader(inputfile)

	# Extract first row to avoid appending to revenue_change_list
	first_row = next(reader)
	total_months = total_months + 1
	total_revenue = total_revenue + int(first_row["Profit/Losses"])
	prev_revenue = int(first_row["Profit/Losses"])



	for row in reader:
		#The total number of months included in the dataset
		total_months = total_months + 1
		#The net total amount of "Profit/Losses" over the entire period
		total_revenue = total_revenue + int(row["Profit/Losses"])
		#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
		revenue_change = int(row["Profit/Losses"]) - prev_revenue
		prev_revenue = int(row["Profit/Losses"])
		revenue_change_list = revenue_change_list + [revenue_change]
		month_of_change = month_of_change + [row["Date"]]

		#The greatest increase in profits (date and amount) over the entire period
		if revenue_change > greatest_increase:
			greatest_increase = revenue_change
			greatest_increase_month = row["Date"]

		#The greatest decrease in losses (date and amount) over the entire period
		if revenue_change < greatest_decrease:
			greatest_decrease = revenue_change
			greatest_decrease_month = row["Date"]

revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase} (${greatest_increase_month})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease} (${greatest_decrease_month})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(ofile, "w") as txt_file:
    txt_file.write(output)