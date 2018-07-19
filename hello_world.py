# print('hello world!')
# print('The answer is ', 9+1, '.', sep='')
# print('hi', 'there', sep='\n')
print('Hi', end=' ')
print('Kendrick')
f = open('hello.txt', 'w')
print('Hi Zach', file=f)
ans = input('How are you? ')
if ans in ('good', 'great', 'well'):
    print('I\'m glad to hear you are ', ans, '. What are you doing later? ', sep='')
    Response = input()

elif ans == 'bad' or ans == 'horrible' or ans == 'shitty' or ans == 'shit':
    print('I\'m sorry to hear you are ', ans, ' today.', ' What are you doing later?', end='', sep='')


# print(ans == ' good' or ans == ' well')

# print(len(ans))
# smallest_number = min(6, 17, 10, -1)
# print(smallest_number)




