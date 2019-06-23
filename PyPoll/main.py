import os
import csv
csv_file_to_open = 'election_data.csv'
path_election_data_file_csv = os.path.join('Election.csv')


def profile_per_candidate(dataset, total_votes):
    lcandidate = {'stats':{}}
    for candidate in dataset:    
        if candidate[2] not in lcandidate.items():
            lcandidate['stats'][candidate[2]] = 0

    votes_number = 0
    for name in lcandidate['stats']:
        for rows in dataset:
            if rows[2] == name:
                votes_number +=1
                lcandidate['stats'][name] = [votes_number]
                lcandidate['stats'][name].append(100 * votes_number/total_votes)
                lcandidate['stats'][name].append(0)
        votes_number = 0
    
    winner = 0
    for c in lcandidate['stats']:
        if lcandidate['stats'][c][0] > winner:
            winner = lcandidate['stats'][c][0]
            lcandidate['stats'][c][2] = 1
        else:
            lcandidate['stats'][c][2] = 0
    return lcandidate

def poll_results():
    #Dict where all data will be allocated
    election_results = {
            'headers': ['  ELECTION RESULTS  ', '-------------------------'],
            'votes': 0,
            'labels': ['Total Votes', 'Winner'],
            'candidates': {}
            }
    
    with open(path_election_data_file_csv, 'r') as election_data_file:
        election_data_ds = csv.reader(election_data_file, delimiter=',')
        next(election_data_ds)
        
        #Comprehension list of elections.
        election_data_list = [election for election in election_data_ds]
        
        #Get total votes, no matter the candidate.
        election_results['votes'] = len(election_data_list)
        #Get profile for each candidate
        election_results['candidates'] = profile_per_candidate(election_data_list, election_results['votes'])
        
        #Print out Election Results
        print("")
        print(f"{election_results['headers'][0]}\n{election_results['headers'][1]}")
        print(f"{election_results['labels'][0]}: {election_results['votes']}")
        print(f"{election_results['headers'][1]}")
        for candidate in election_results['candidates']['stats']:
            print(f"{candidate}: {election_results['candidates']['stats'][candidate][1]:.3f}% ({election_results['candidates']['stats'][candidate][0]})")
        print(f"{election_results['headers'][1]}")
        for winner in election_results['candidates']['stats']:
            if int(election_results['candidates']['stats'][winner][2]) == 1:
                print(f"      {election_results['labels'][1]}: {winner}  ")
                break
        print("")


poll_results()
