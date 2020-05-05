# Import dependecies
import os
import csv
import pandas as pd
dataset = pd.read_csv('Resources/budget_data.csv')

# The net total amount of "Profit/Losses" over the entire period
def profit (dataset):
    profit = dataset['Profit/Losses'].sum()
    return profit

#The average of the changes in "Profit/Losses" over the entire period
def avg(dataset): 
    dataset['change'] = dataset['Profit/Losses'] - dataset['Profit/Losses'].shift(1)
    avg_change = round((dataset['change'].sum()/(len(dataset)-1)),2)
    return avg_change

#The greatest increase in profits (date and amount) over the entire period
def best (dataset):
    best_increase = dataset['change'].max()
    row = dataset.loc[dataset['change'] == best_increase]
    best_date = row.iloc[0]['Date']
    return best_date, best_increase

#The greatest increase in profits (date and amount) over the entire period
def worst (dataset):
    best_decrease = dataset['change'].min()
    row = dataset.loc[dataset['change'] == best_decrease]
    worst_date = row.iloc[0]['Date']
    return worst_date, best_decrease

#Run the program and print the result 
def report(dataset):
    # The total number of months included in the dataset
    months = len(dataset)
    profit_rep = profit(dataset)
    avg_change_rep = avg(dataset)
    best_date_rep = best(dataset)[0]
    best_increase_rep = best(dataset)[1]
    worst_date_rep = worst(dataset)[0]
    best_decrease_rep = worst(dataset)[1]
    print ("")
    print ("Financial Analysis")
    print ("--------------------")
    print (f'Total Months: {months}') 
    print (f'P & L : ${profit_rep}')
    print (f'Average change: ${avg_change_rep}')
    print (f'Greatest Increase in Profits: {best_date_rep} ${best_increase_rep}')
    print (f'Greatest Decrease in Profits: {worst_date_rep} ${best_decrease_rep}')
    print ("")
    
report(dataset)