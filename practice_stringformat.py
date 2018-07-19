


things = ['camera', 'couch', 'potato salad', 'energy drink', 'comb', 'suitcase']
prices = [50, 100, 5, 5, 1, 25]

for i in range(len(things)):
    # things[0]
    print('{0:>12}: ${1:>7.2f}'.format(things[i], prices[i]))