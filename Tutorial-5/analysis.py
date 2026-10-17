#Made By Ricky L.

import binarycount
import improvedqueue
import random
import time

xMax = random.randint(0,12409812093481290)
yMax = random.randint(0,1209840912904381209390129031902590189024890123123)
X = [random.randint(0,xMax) for i in range(2500)]
Y = [random.randint(0,yMax) for i in range(50000)]

X.sort()

for y in Y:
    if binarycount.count(X,y) != X.count(y):
        print("Mismatch Detected for",y)

start = time.time()
for y in Y:
    X.count(y)
end = time.time()
linearTime = end - start

start = time.time()
for y in Y:
    binarycount.count(X,y)
end = time.time()
binaryTime = end - start

print("Linear list.count() time:",linearTime)
print("Binary count time:",binaryTime)

print(f'Binary count was {linearTime/binaryTime:.2f}x faster than Linear count') if binaryTime < linearTime else print(f'Linear count was {binaryTime/linearTime:.2f}x faster than Binary count')

'''
QnA

1. Binary search count is a lot faster than linear count. On average, it is about at least 12x faster.
2. The bigger X is, the slower Linear search gets.
3. Timing does not really change between both Binary and Linear.
4. The more missing values => the more faster Binary gets compared to Linear for the same exact search. 
5. Based on the results, the time complexity for all of those test runs makes sense. Binary search will overall be faster due to it's O(log n) time complexity compared to linear's O(n) time complexity


'''

