import random

# won = False
#
# Win = random.randint(1, 5)
# while won == False:
#     guess = int(input('Guess the Number: '))
#     message = 'You Win.'
#     if guess > Win:
#         print('Number is too high.')
#     elif guess < Win:
#         print('Number is too low.')
#     elif guess == Win:
#         print(message)
#         won = True



Job = input('Would you like to apply for a Job? ')
while Job != 'no' or Job != 'No' or Job.lower() != 'yes' or Job != 'i guess' or Job != 'probably' or Job != 'prob':
    if Job == 'no' or Job == 'No':
        print('Goodbye!')
    elif Job.lower() == 'yes' or Job == 'i guess' or Job == 'probably' or Job == 'prob':
        Exp = input('Do you have job experience? ')
        if Exp.lower() == 'no':
            print('You may apply for an entry level position.')
        elif Exp == 'yes' or Exp == 'Yes':
            Years = input('How many years of experience do you have? ')
            if int(Years) >= 3:
                print('You may apply for a advanced position.')
            elif int(Years) < 3:
                print('You may apply for a mid-level position.')
            else:
                print('Please enter number amount of years. (ex. 1, 2, 3, 4...)')
        else:
            print("Please type 'yes' or 'no'")
    else:
        print("Please type 'yes' or 'no'")
        Job = input()

# dice_one = random.randint(1, 6)
# dice_two = random.randint(1, 6)
#
# if dice_one == dice_two or dice_one + dice_two == 6 or dice_one + dice_two ==3:
#     print('You Win!')
# else:
#     print("You Lost.")

