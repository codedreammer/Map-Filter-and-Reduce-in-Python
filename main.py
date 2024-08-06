#MAP
'''def cube(x):
    return x*x*x

print(cube(2))

l = [1,2,4,6,7,3]

newl = list(map(cube, l))
print(newl)
'''
l = [2,4,6,7,8,9]

nwel = list(map(lambda x: x*x*x ,l))
print(nwel)

k = [2,4,5,7,8,9]
newk = list(map(lambda x: x*x, k))
print(newk)

#FILTER
a = [2,4,5,7,9,10]

def filter_function(b):
    return b>2

newnewl = list(filter(filter_function, a))
print(newnewl)

#REDUCE

from functools import reduce

numbers = [1,2,5,6,8,9]

def mysum(x, y):
    return x + y

sum = reduce(mysum, numbers)

print(sum)

from functools import reduce

lists = [3,4,6,78,8,5,7]

def mysum(x, y):
    return x + y
sum = reduce(mysum, lists)
print(sum)
