# print(int(-2.9))
# year = input('Enter your year of birth:')
# print('You are around', end=' ')
# print(2018-int(year), end=' ')
# print('years of age', '.', sep='')
# a = 3
# b = 5
#c = 7
# Print true if a<b and b<c
# Also print True if a>b and b>c
#print((a < b and b < c) or (a > b and b > c))
import random
year = random.randint(1000,2018)
# Use % if year is divisible by 4
# Unless it's divisible by 100
# It's okay to be divisible by 100
# If also divisible by 400
print(year, 'was a leap year.')
print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

# First_number = input('Type in First Number:')
# Second_number = input('Type in Second Number')
# Third_number = input('Type in Third Number')
# print((int(First_number) * int(Second_number))/int(Third_number))
#
# Number = input('Enter a Number, True = Even and False = Odd:')
# print(int(Number) % 2 == 0)

Money = input('Enter Amount of Money in Dollars:  $ ')
print('$', Money, ' is ', int(Money) * .86, ' Euros', sep='')

# Name = input('Enter Your Name: ')
# print((ord(Name[0])))

print(vars())


