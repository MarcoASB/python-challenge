import os
import csv
csv_file_to_open = 'election_data.csv'
path_election_data_file_csv = os.path.join('Election.csv')


def profile_per_candidate(dataset, total_votes):
    lcandidate = {'stats':{}}
    #A complete list of candidates who received votes
    for candidate in dataset:    
        if candidate[2] not in lcandidate.items():
            lcandidate['stats'][candidate[2]] = 0
    
    #The total number of votes each candidate won
    #The percentage of votes each candidate won
    votes_number = 0
    for name in lcandidate['stats']:
        for rows in dataset:
            if rows[2] == name:
                votes_number +=1
                lcandidate['stats'][name] = [votes_number]
                lcandidate['stats'][name].append(votes_number/total_votes*100)
                lcandidate['stats'][name].append(0)
        votes_number = 0
    
    #The winner of the election based on popular vote.
    winner = 0
    for c in lcandidate['stats']:
        if lcandidate['stats'][c][0] > winner:
            winner = lcandidate['stats'][c][0]
    return lcandidate

def poll_results():
    election_results = {
            'headers':'  ELECTION RESULTS  ',
            'separate': " ---------------------- ",
            'votes': 0,
            'labels': ['Total Votes', 'Winner'],
            'candidates': {}
            }
    
    with open(path_election_data_file_csv, 'r') as election_data_file:
        election_data_ds = csv.reader(election_data_file, delimiter=',')
        next(election_data_ds)
        election_data_list = [election for election in election_data_ds]
        #The total number of votes cast
        election_results['votes'] = len(election_data_list)
        election_results['candidates'] = profile_per_candidate(election_data_list, election_results['votes'])
        
        #Print out Results
        print("")
        print(f"   {election_results['headers']}")
        print(f"{election_results['labels'][0]}: {election_results['votes']}")
        print(f"{election_results['separate']}")
        for candidate in election_results['candidates']['stats']:
            print(f"{candidate}: {election_results['candidates']['stats'][candidate][1]:.3f}% ({election_results['candidates']['stats'][candidate][0]})")
        print(f"{election_results['separate']}")
        for winner in election_results['candidates']['stats']:
            if int(election_results['candidates']['stats'][winner][2]) == 1:
                print(f"           {election_results['labels'][1]}: {winner}  ")
                break
        print("")


poll_results()
