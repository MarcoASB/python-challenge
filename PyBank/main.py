import os
import csv
filepath = os.path.join('PyBank.csv')

#The net total P&L over the entire period of analysis
def profit (dataset):
    result = 0
    for PL_row in dataset: 
        result += int(PL_row[1])
    return result


#The average of the changes in "Profit/Losses" over the entire period
def avg(dataset): 
    result = 0
    Tot_change = 0  
    for PL_row in range(len(dataset)-1):
        first = float(dataset[PL_row][1])
        second = float(dataset[PL_row+1][1])
        PL_change = second - first
        Tot_change += PL_change
    result = round(Tot_change / (len(dataset)-1),2)     
    return result   


#The greatest increase in profits (date and amount) over the entire period
def best (dataset):
    result = []
    month = ''
    max_change = 0
    for PL_row in range(len(dataset)-1):
        first = float(dataset[PL_row][1])
        second = float(dataset[PL_row+1][1])
        current_change = second - first
        if current_change > max_change:
            max_change = current_change
            month = str(dataset[PL_row+1][0])                  
    result.append(month)
    result.append(round(max_change))     
    return result


#The greatest increase in profits (date and amount) over the entire period
def worst (dataset):
    result = []
    month = ''
    min_change = 0
    for PL_row in range(len(dataset)-1):
        first = float(dataset[PL_row][1])
        second = float(dataset[PL_row+1][1])
        current_change = second - first
        if current_change < min_change:
            min_change = current_change
            month = str(dataset[PL_row+1][0])                  
    result.append(month)
    result.append(round(min_change))     
    return result


#Run the program and print the result 
def report():
    with open(filepath,'r') as csvfile:
        reader =csv.reader(csvfile,delimiter=',')
        next(reader, None)
        budget_data=[month for month in reader]  
        #The total number of months included in the dataset
        months = len(budget_data)
        get_PL = profit(budget_data)
        get_avg = avg(budget_data)
        get_best = best(budget_data)
        get_worst = worst(budget_data)
    print ("")
    print ("Financial Analysis")
    print("--------------------")
    print (f'Total Months: {months}') 
    print (f'P & L : ${get_PL}')
    print (f'Average change: ${get_avg}')
    print (f'Greatest Increase in Profits: {get_best[0]} ${get_best[1]}')
    print (f'Greatest Decrease in Profits: {get_worst[0]} ${get_worst[1]}')
    print ("")


report()

