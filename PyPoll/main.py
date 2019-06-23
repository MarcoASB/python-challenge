import os
import csv
filepath = os.path.join('Election.csv')

def report():
    with open(filepath,'r') as csvfile:
        reader =csv.reader(csvfile,delimiter=',')
        next(reader, None)
        vote_count=[vote for vote in reader]  
        #The total number of months included in the dataset
        total_votes = len(vote_count)
    print("")
    print("     ELECTION RESULTS     ")
    print("--------------------------")
    print(f"  Total votes :  {total_votes}")
    print("--------------------------")
    print(f'{c_list[0]} {} {}')
    print(f'{c_list[1]} {} {}')
    print(f'{c_list[2]} {} {}')
    print(f'{c_list[3]} {} {}')
    print("")



def candidates_list(dataset):
    c_list =[]
    for x in reader:
        if x[2] not in c_list.items():
            c_list.append(x)

