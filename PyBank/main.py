#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
os.chdir("GitHub\Module3\python-challenge\Resources")

# Read the CSV file into a DataFrame
df = pd.read_csv("budget_data.csv")

# Calculate the month-over-month (MoM) change in Profit/Losses
df["Profit/Losses_change"] = df["Profit/Losses"].diff()

# Calculate the total number of months
total_months = len(df)

# Calculate the total Profit/Losses
total_ProfitLosses = df["Profit/Losses"].sum()

# Calculate the average month-over-month Profit/Losses change
average_change = df["Profit/Losses_change"].mean()

# Find the greatest increase in profit and its corresponding month
greatest_increase = df["Profit/Losses_change"].max()
greatest_increase_month = df.loc[df["Profit/Losses_change"] == greatest_increase, "Date"].values[0]

# Find the greatest decrease in profit and its corresponding month
greatest_decrease = df["Profit/Losses_change"].min()
greatest_decrease_month = df.loc[df["Profit/Losses_change"] == greatest_decrease, "Date"].values[0]

# Create the desired output format
output = "Financial Analysis\n"
output += "----------------------------\n"
output += f"Total Months: {total_months}\n"
output += f"Total: ${total_ProfitLosses:.2f}\n"
output += f"Average Change: ${average_change:.2f}\n"
output += f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase:.0f})\n"
output += f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease:.0f})\n"

# Print the output to the console
print(output)

# Export the output to a text document
with open("financial_analysis.txt", "w") as text_file:
    text_file.write(output)

