import re
import sys

try:
    f = open('z/Users/kendrickberman/Desktop/harrypotter.txt', 'r')

    text = f.read()

    f.close()

    print(text[:1000])

    harry_quotes = re.findall('".*".*Harry.*', text)

    print(harry_quotes)

    for quote in harry_quotes:
        print(quote)


except:

    print('You got an Error yo')
    print(sys.exc_info()[0])

