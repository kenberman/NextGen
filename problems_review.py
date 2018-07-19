# ans = input('Type in a word and I will give you the plural of it: ')
# if ans[-1] in ('x', 's'):
#     print(ans, 'es', sep='')
# elif ans[-2:] in ('th', 'sh', 'ch'):
#     print(ans, 'es', sep='')
# else:
#     print(ans, 's', sep='')


# Bin-max



places = 20

for n in range(256):

    highest_num = 0  #reset highest num

    #computes higest num for n-places
    for p in range(n):
        highest_num += (2 ** p)  # Add up binary value

    print(n, 'bits lets you go up to', highest_num)

