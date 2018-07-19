import random
import statistics
import time

Number = input('Guess from 1-10: ')
print('Are you a winner? ', end='', flush=True)
time.sleep(1)
Random = random.randint(1, 10)
if Number == Random:
    print('You Won!')
elif int(Number) > int(Random):
    print('Too high! You lost.')
else:
    print('I\'m sorry. You lost.')

time.sleep(1.0)
print('The secret number was', Random)
# time.sleep(1)

# ages = (18, 20, 21, 17, 15, 16, 20, 18, 21, 17, 22, 14, 20)
# print(statistics.median(ages))
# print(statistics.mode(ages))


print('How old are you? ', end='')
age = input()
age = int(age)
#check age
if age >= 18:
    #show news
    news = "Riots in the Streets."
    print(news)
if age < 18:
    restricted = "You are too young to view this website."
    print(restricted)




