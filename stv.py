import pandas as pd
import numpy as np

def get_parameters(course_count): #get user input
    """Ask the user for the number of courses to select using while
    loop to ensure a valid number is entered. Gets df index lenght
    as input"""
    while True:
        try:
            course_no = int(input('\nPlease enter the number of courses to select. The maximum number of courses is {}: '.format(course_count)))
            if course_no <= course_count:
                break
        except KeyboardInterrupt: #To allow terminating the program during input
            print('\n')
            break
        except:
            print('\nThat\'s not a valid city number! Select a number between 1 and {}: \n'.format(course_count))

    print('-'*40)
    return course_no

def voting_summary(voting_data):
    """right now just producing dataframe with sum of votes for each courses
    """
    voting_sum = voting_data.apply(pd.value_counts)
    return voting_sum

#load the survey data into a DataFrame and drop all NaN rows
voting_data = pd.read_csv('americas.csv').dropna(thresh=1)
#determine the number of courses offered
votes_count  = len(voting_data.index)
#get number of courses available to pick from
course_count = voting_data.shape[1]
#get courses to select from user
course_no = get_parameters(course_count)
#Calculate the threshhold for winners
droop_quota = (votes_count/course_no + 1) + 1
#create Series to count votes
vote_tally = pd.DataFrame({'Votes' : pd.Series(data = [0] * course_count, index = list(voting_data))})
#Voting summary of each course by priority
voting_table = voting_summary(voting_data).dropna(thresh=1)
voting_table.to_csv(r'Tally.csv') #export to CSV to verify


print('\nThere are {} courses and you chose to pick {}.\n'.format(course_count, course_no)) #temp as a test of load
print('The Droop Quota is {}\n'.format(droop_quota))
print('-'*40)
print(vote_tally)
print('-'*40)
print(voting_table)
