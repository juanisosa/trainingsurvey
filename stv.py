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
    #Calculate the threshhold for winners
    #droop_quota = int(len(voting_data.index)/course_no + 1) + 1
    #print('\nThe Droop Quota is {}\n'.format(droop_quota))
    #create Series to count votes
    vote_tally = voting_sum.loc[1].fillna(0)
    loser = voting_sum.sum().idxmin()
    print('\n{} has {} votes\n'.format(loser, vote_tally.min()))
    voting_sum.to_csv('tally.csv')
    #for 
    #voting_data = voting_data.drop(vote_tally.(insert argument to find list of courses with 0 votes), axis=1)
    '''while vote_tally.size > course_no:
        print(loser)
        if voting_sum[loser].sum() == 0:
            print('no votes')'''


    #i = 2
    '''while i < course_no:
        vote_round_result = voting_sum.loc[i].fillna(0)
        vote_tally = vote_tally + vote_round_result
        i += 1'''
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
