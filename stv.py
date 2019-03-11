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

#load the survey data into a DataFrame and drop all NaN rows
voting_data = pd.read_csv('americas.csv').dropna(thresh=1).dropna(axis='columns', thresh=1)

#get courses to select from user
course_no = get_parameters()

#perform a round of counting
"""Voting summary of each course by priority as a dataframe with rows for
each priority"""
voting_sum = voting_data.apply(pd.value_counts)
voting_sum.to_csv('voting_sum.csv')

#create Series to count votes with priority 1 and drop courses with no votes
vote_tally = voting_sum.loc[1].dropna()
print('\nRound Count Results')
print(vote_tally)
print('-'*40)

print('\n{} courses got votes and there are {} slots to fill.\n'.format(len(vote_tally), course_no))

if len(vote_tally) > course_no:
    print('One more round')

    while len(vote_tally) > course_no:

        '''determine loser course of round firt we find series of courses with
        fewest votes as option 1'''

        losers = vote_tally.loc[vote_tally == vote_tally.min()].index.tolist()

        #conditional statement to find loser based on losers list
        if len(losers) == 1:
            loser = losers[0]
        #if tie then losers length > 1 then we do while loop to look at tie breaker based on number of next priority
        elif len(losers) > 1:
            i = 2
            tie_breaker = voting_sum.loc[i, losers].fillna(0)
            tie_breaker = tie_breaker.loc[tie_breaker == tie_breaker.min()].index.tolist()
            if len(tie_breaker) == 1:
                loser = tie_breaker[0]
            else:
                while len(tie_breaker) > 1:
                    i += 1
                    tie_breaker = voting_sum.loc[i, tie_breaker].fillna(0)
                    tie_breaker = tie_breaker.loc[tie_breaker == tie_breaker.min()].index.tolist()
                    loser = tie_breaker[0]

        #create list of courses that move to next round by removing loser from vote_tally
        next_round = vote_tally.index.tolist()
        next_round.pop(next_round.index(loser))

        '''figure out how to substract 1 from rows in americas.csv where the loser received first ranking'''

elif len(vote_tally) == course_no:
    print('The courses bellow are the chosen ones and their respective votes:')
    print(vote_tally)
elif len(vote_tally) < course_no:
    print('Not enough votes were received to fill all training slots offered. This was the results:')
    print(vote_tally)
