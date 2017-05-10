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
    outfile.write('The square root is: ')
    outfile.write(str(sqrt + '\n'))
    outfile.write('The number raised to the power of 3 is: ')
    outfile.write(str(powr + '\n'))
    outfile.close()
while another != 'y' or another != 'Y':
    infile = open('numbers.txt', 'r')
    contents = infile.read()
    infile.close()
    print('Here is what you have entered: ')
    print(contents)
