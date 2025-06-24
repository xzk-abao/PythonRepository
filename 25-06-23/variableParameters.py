from typing import Iterable
from unittest import result


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)



def fact(n):
    """Calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3]


def findMinAndMax(L):


    maxNum = L[0]
    minNum = L[0]
    for x in L:
        if x > maxNum:
            maxNum = x
        if x < minNum:
            minNum = x
    
    print('maxNum:', maxNum, 'minNum:', minNum)
    return (maxNum, minNum)

L = ['Hello', 'World', 18, 'Apple', None]

[s.lower() for s in L if isinstance(s, str)]


def triangles():
    L = []
    size = 1
    while size < 12:  # 这里直接写10
        for i in range(size):
            L.append(i)
        yield L
        L = []
        size += 1  # 修正这里

n = -1
result = []
for t in triangles():
    result.append(t)
    n = n + 1
    if n == 10:
        break
for t in result:
    print(t)
print('result:', result)