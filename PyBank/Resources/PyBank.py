# import libraries
import csv
import os

# load and output
# file_to_load = csvpath = "budget_data.csv"
# file_to_output = csvpath = "budget_analysis.txt"
file_to_load = os.path.join("budget_data.csv")
file_to_output = os.path.join("budget_analysis.txt")

# track parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

# read header
    header = next(reader)

# extracting first row from net_change_list
    first_row = next(reader)
    total_months +=1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

# track the total
        total_months += 1
        total_net += int(row[1])

# track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

# calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
# calculate greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# calculate avg net change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# generate output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg: .2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    


#  print output to terminal
print(output)

# export to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


