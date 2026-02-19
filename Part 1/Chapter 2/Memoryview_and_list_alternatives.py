from array import array
from random import random
import numpy as np

# arrays have in-built read/write functions to files which gives them use cases over lists
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
with open('floats.bin', 'wb') as f:
    floats.tofile(f) # writes floats as binary to file
    f.close()

floats2 = array('d')
with open('floats.bin', 'rb') as f:
    floats2.fromfile(f, 10**7)
    f.close()
print(floats2[-1])

print(floats == floats2)

# arrays should also be preferred to save memory when we have large numerical values storage


# memoryview (generalized numpy array structure without the math) -

octet = array('B', range(6)) # B is for unsigned char (int between 0-255)
print(octet)
m1 = memoryview(octet) # build memoryview
print(m1.tolist()) # export it to list to print

m2 = m1.cast('B', [2, 3]) # returns another memoryview object, sharing memory with m1
print(m2.tolist()) # create matrix of shape(2, 3)

m3 = m1.cast('B', [3, 2])
print(m3.tolist()) # create matrix of shape(3, 2)

print(m2[1, 1])

m2[1, 1] = 22
m3[2, 1] = 33

print(octet.tolist()) # original array was changed by change in m2 and m3
# because memoryview enables sharing memory between data structures

'''
m1 which was [0, 1, 2, 3, 4, 5]
when we do m2 = m1.cast(some shape)
we are viewing the same memory object (m1) but in a different shape
'''


# deque
from collections import deque

# whenever we have data sequence where we have to access or operate on elements on either
# end of the sequence, deques are highly effective

dq = deque(range(10), maxlen=10) # maxlen sets len limit to deque

dq.rotate(3) # rotate modifies deque in-place
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(5) # 0 on right will be removed from deque as maxlen is 10
print(dq)

dq.extendleft([6, 7, 8]) # 9, 8, 7 on the right removed due to maxlen
print(dq)
