#this code will take the average of user inputted test scores and give the actual
#average and also the average rounded up to the next whole number
import math # required to use the math modules
total = 0 #set the accumulator for total to zero 
another = 'y' #set the variable another = y for the while loop
count = 0 #set the count accumulator to zero
while another == 'y' or another == 'Y':
    #have the user enter a test score
    score = float(input('Enter the score for a test: '))
    #add that test score to the total value for test scores
    total += score
    #ask the user if they have another score to add in
    another = input('Would you like to add another score? ' + \
                    '(Enter y or Y for yes):')
    #if else statement for the result of the while loop
    if another == 'y' or another == 'Y':
        count = count + 1
    else:
        print('The total of the scores is: ', format(total, '.2f'))
        print('The actual average of your scores is: ', format((total / count), '.2f'))
        print('The average of your scores(rounded up) is: ', (math.ceil(total / count)))
