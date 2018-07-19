#1

def find_max(a, b, c):
    '''
    find maximum of three numbers
    '''

    maximum = max(a, b, c)
    return maximum


#2
def sum(numbers):


    total = 0
    for x in numbers:
        total += x
    return total


#3

def mult(numbers):


    total = 1
    for x in numbers:
        total *= x
    return total


#4
def reverse(string):


    rev = string[::-1]
    return rev


#5
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


  #6
def check_range(choice, numbers):
        answer = None
        i = 0
        for y in numbers:
            if choice == y:
                answer = True
                i = 1
            elif choice != y and i == 0:
                answer = False
        if answer == True:
            end = choice, "is in the range", numbers
        elif answer == False:
            end = choice, "is not in the range", numbers
        return end

#7
def detect_caps(word):
    count_uppers = 0
    count_lowers = 0

    # GO through word and count uppercase and lowercase


    for w in word:
        if w == w.lower():
            count_lowers += 1
        elif w == w.upper():
            count_uppers += 1
    return (count_uppers, count_lowers)


#9

def check_prime(num):
    for x in num:
        if x > 1 and x%1 and x%x:
            print('Prime')
        else:
            print('Not Prime')
    







# a = find_max(5, 6, 10)
# print(a)
#
# print(sum((3, 4, 5, 6, 7)))
#
# print(mult((5, 3, 1, 2)))
#
# print(reverse('KENDRICK BERMAN'))
#
# print(factorial(5))
#
# print(check_range(5, (5, 4, 6, 12, 56)))
#
# t = detect_caps('KendrIck')
# print("Upper Case Letters: ", t[0])
# print('Lower Case Letters: ', t[1])
