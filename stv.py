import time
import pandas as pd

def get_parameters(course_count):
    #Ask the user for the number of courses to select using while loop to ensure a valid number is entered. Gets df index lenght as input
    while True:
        try:
            course_no = int(input('\nPlease enter the number of courses to select. The maximum number of courses is {}: '.format(course_count)))
            if course_no <= course_count:
                break
        except KeyboardInterrupt: #To allow terminating the program during input
            print('\n')
            break
        except:
            print('\nThat\'s not a valid city number! Select a number between 1 and {}: '.format(course_count))

    print('-'*40)
    return course_no

#We load the survey data into a DataFrame
voting_data = pd.read_csv('americas.csv')
course_count = len(voting_data.index) #determine the number of courses offered in survey
course_no = get_parameters(course_count) #get courses to select from user


print('There are {} courses and you chose to pick {}.'.format(course_count, course_no)) #temp as a test of load
