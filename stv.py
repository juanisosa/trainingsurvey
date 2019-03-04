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
    
    
voting_data = pd.read_csv('americas.csv') #load the survey data into a DataFrame
votes_count  = len(voting_data.index) #determine the number of courses offered in survey
course_no = get_parameters(course_count) #get courses to select from user
droop_quota = (votes_count/course_no + 1) + 1 #Calculate the threshhold for votes
vote_tally_list = [0] * voting_data.shape[1] #get number of courses avilable to choose from
vote_tally = pd.series(data = vote_tally_list, index = list(voting_data)) #create series to count votes

print('\nThere are {} courses and you chose to pick {}.\n\n'.format(course_count, course_no)) #temp as a test of load
print('-'*40)
print(voting_data['index'])
