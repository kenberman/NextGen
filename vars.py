t = 9
name = 'Mr. T'
animal = 'hippo'


d = vars().copy()

for k in d:
    if '__' not in k:
        print(k, ':', d[k])


print('__name__ = ', d['__name__'])



