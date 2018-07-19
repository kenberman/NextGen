text = 'How are you today good sir? I hope you are well.'

# Get rid of punctuation
# punctuation = ('?', '.', ',', '(', ')')
#
# for p in punctuation:
#     text = text.replace(p, '')

# split text into a tuple
# text_tuple = tuple(text.split())

# display word count
# print(text_tuple)
# print('There are', len(text_tuple), 'words')
#
#
# names = ('Kathy', 'Benji', 'Ian', 'Alejandro')
#
# for n in names:
#     print(n, ':', len(n), "letters")

import random


firstnames = ('Frances', 'Perry', 'Kerry', 'Omar', 'Carmen', 'Sonia', 'Eloise', 'Trevor', 'Ricardo', 'Tyler')

lastnames = ('Blake', 'Cannon', 'Ball', 'Munoz', 'Webb', 'Doyle')

num_names = int(input('How many names? '))


for n in range(num_names):
    print(random.choice(firstnames), random.choice(lastnames))

total = 0
while total < num_names:
    print(random.choice(firstnames), random.choice(lastnames))
    total += 1
