import math
outfile = open('numbers.txt', 'w')
another = 'y'
while another == 'y' or another == 'Y':
    number = float(input('Enter a number to be calculated: '))
    sqrt = format(math.sqrt(number), '.2f')
    powr = format(math.pow(number, 3), '.2f')
    print('The square root of your number is: ', sqrt)
    print('Your number raised to the power of 3 is: ', powr)
    another = input('Would you like to calculate another number?' + \
                    '(Enter y for yes):')
if another == 'y' or another == 'Y':
    infile = open('numbers.txt', 'r')
    contents = infile.read()
    infile.close()
    print(contents)
else:
    outfile.write(str('The square root is: ', 'sqrt\n' + \
                      'and the number raised to the power of 3 is: ' 'powr\n'))
    outfile.close()
