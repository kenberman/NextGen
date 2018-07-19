def make_double (a):
    '''

    Doubles the Number
    '''
    dbl = a * 2
    return dbl   # return value

def make_half (a):


    half = a / 2
    return half

def make_plural(word):
    return word + 's'


def get_power(base, exp):

    '''
    Raise base to the power of exp
    :param base:
    :param exp:
    :return:
    '''

    return base ** exp




print(get_power(8,2))
print(make_plural('hat'))

b = make_double(5)
print(b)

c = make_half(10)
print(c)

