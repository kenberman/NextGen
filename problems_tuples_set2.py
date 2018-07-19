import random

word = random.choice(('Dog', 'Bird', 'Truck')).lower()


for w in word:
    print('_ ', end='')

#keep playing until the user wins
#keep playing until guesses run out
guesses = len(word) + 3
correct_guesses = ()



while guesses > 0 and len(word) != len(correct_guesses):
    letter = input('      Guess a letter: ').lower()

    if letter.lower() in word.lower() and letter.lower() not in correct_guesses:
        print('Correct')
        correct_guesses = correct_guesses + (str(letter),)
        print(correct_guesses)
    elif letter.lower() in correct_guesses:
        print('You already guessed that. Guess a different letter. ')
    else:
        print('Horrible guess. ')
        guesses -= 1

    for w in word:
        if w in correct_guesses:
            print(w, end='')
        else:
            print('_ ', end='')


if len(word) != len(correct_guesses):
    print('You won!')
