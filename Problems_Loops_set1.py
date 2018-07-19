import random
import time


guess = random.randint(1, 10)
Number = input('Think of a number between 1-10, I will try to guess it. When ready hit ENTER ')
print('Is it ', guess, '?', sep='')
answer = input()
#
Trys = 5
#
while answer.lower() == 'no' and Trys > 1:
    guess = random.randint(1, 10)
    print('Is it ', guess, '?', sep='')
    Trys -= 1
    answer = input()
if answer.lower() == 'yes':
    print('I won!')
else:
    print('You ran out of tries.')

# Password = input('Create a Password: ')
# while len(Password) < 8 or Password.lower() == Password:
#     print('Password must have 8 or more characters and have at least one uppercase.')
#     Password = input('Create a Password: ')
# else:
#     print('Password Created.')

# for name in 'Jen', 'April', 'Neil', 'Stu':
#     print('Hi', name)
#     time.sleep(1)
#
# for i in range(1, 20):
#     print(i)
#
# for c in "baseball":
#     if c in "aeiou":
#         print(c)








