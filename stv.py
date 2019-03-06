import pandas as pd
import numpy as np

def get_parameters(): #get user input
    """Ask the user for the number of courses to select using while
    loop to ensure a valid number is entered. Gets df index lenght
    as input"""
    #get number of courses available to pick from
    course_count = voting_data.shape[1]
    while True:
        try:
            course_no = int(input('\nPlease enter the number of courses to select. The maximum number of courses is {}: \n'.format(course_count)))
            if course_no <= course_count:
                break
        except KeyboardInterrupt: #To allow terminating the program during input
            print('\n')
            break
        except:
            print('\nThat\'s not a valid city number! Select a number between 1 and {}: \n'.format(course_count))

    print('-'*40)

    print('\nThere are {} courses and you chose to pick {}.\n'.format(course_count, course_no)) #temp as a test of load

    print('-'*40)
    return course_no

def counting_votes(voting_data, course_no):
    #Voting summary of each course by priority
    voting_sum = voting_data.apply(pd.value_counts)

    #create Series to count votes and drop courses with no votes
    vote_tally = voting_sum.loc[1].dropna()

    #create list of courses that move to next round
    next_round = vote_tally.index.tolist()
    print(next_round)
    #determine loser course of round
    loser = vote_tally.idxmin()
    print('\n{} has {} votes\n'.format(loser, vote_tally.min()))


    return vote_tally

#load the survey data into a DataFrame and drop all NaN rows
voting_data = pd.read_csv('americas.csv').dropna(thresh=1).dropna(axis='columns', thresh=1)
voting_data.to_csv('americas-no-votes-trimmed.csv')

#get courses to select from user
course_no = get_parameters()

#count the votes with function
winners = counting_votes(voting_data, course_no)



#vote_tally = vote_tally + vote_round_result

print('-'*40)
print('\n')
print(winners)
