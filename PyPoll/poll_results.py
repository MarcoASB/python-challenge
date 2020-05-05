# Import dependecies
import pandas as pd
data = pd.read_csv('Resources/election_data.csv')

# A complete list of candidates who received votes
def candidates (data):
    list_candidates = data.Candidate.unique()
    return list_candidates

# Count and percentage of candidates
def votes (data):
    data['Count'] = 1
    votes = data[['Count','Candidate']].groupby('Candidate').count()
    votes['Percentage'] = round(votes.Count/number_votes*100,2)
    return votes

# The winner of the election based on popular vote.
def winner (data):
    data['Count'] = 1
    votes = data[['Count','Candidate']].groupby('Candidate').count()
    votes['Percentage'] = round(votes.Count/number_votes*100,2)
    max_votes = votes['Count'].max()
    winner_row = votes.loc[votes['Count'] == max_votes]
    winner = winner_row.index[0]
    return winner

def report(data):
    candidates_list = candidates(data)
    can_votes = votes(data)
    can_winner = winner(data)
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: ",len(data))
    print("-------------------------")
    print("{}: {}% ({})".format(candidates_list[0],
                                can_votes.loc[can_votes.index == candidates_list[0]]['Percentage'][0],
                                can_votes.loc[can_votes.index == candidates_list[0]]['Count'][0]))
    print("{}: {}% ({})".format(candidates_list[1],
                                can_votes.loc[can_votes.index == candidates_list[1]]['Percentage'][0],
                                can_votes.loc[can_votes.index == candidates_list[1]]['Count'][0]))
    print("{}: {}% ({})".format(candidates_list[2],
                                can_votes.loc[can_votes.index == candidates_list[2]]['Percentage'][0],
                                can_votes.loc[can_votes.index == candidates_list[2]]['Count'][0]))
    print("{}: {}% ({})".format(candidates_list[3],
                                can_votes.loc[can_votes.index == candidates_list[3]]['Percentage'][0],
                                can_votes.loc[can_votes.index == candidates_list[3]]['Count'][0]))
    print("-------------------------")
    print(f"Winner: ",can_winner)
    print("-------------------------")
    
report(data)