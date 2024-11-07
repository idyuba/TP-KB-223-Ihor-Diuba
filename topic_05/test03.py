# import random
from random import shuffle
from random import randint

someList = [1, 2, 3, 4, 5, 6, 7, 8]
print(someList)

shuffle(someList)
print(someList)

randomId = randint(0, 9)
print(randomId)
print(someList[randomId])