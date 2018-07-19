import random
import time
a = random.randint(0, 10)
print(a * 2)
print(random.choice(('dog', 'cat', 'bird')))
print('Wait for it...')
#time.sleep(5)
print('Gotcha!')
print('challenge...', end='', flush=True)
time.sleep(2)
print('accepted.')
