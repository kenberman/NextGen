import random

secret = random.randint(1, 10)
guess = int(input('Guess a Number from 1-10: '))

while guess != secret:
    if guess > secret:
        print('Too high!', end='')
    else:
        print('Too low!', end='')
    guess = int(input(' Wrong. Guess again: '))

print('You won! The number was', secret)
