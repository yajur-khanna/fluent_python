# Generator expressions are list comprehensions for other sequence types like arrays, tuples
import array

symbols = "@$!"
t = tuple(ord(symbol) for symbol in symbols)

# Important
t = (ord(symbol) for symbol in symbols)
print(t) # we will get a generator object, () doesn't mean it's a list
# when we do tuple(generator object) then we are consuming iterators in gen obj
# using an iterable i.e. a tuple (we could use any other iterator like a list)
print(t)

a = array.array('I', [ord(symbol) for symbol in symbols])
print(a)

# Genexp unlike listcomp produces sequence on the fly

'''
In listcomp -
Python computes all numbers
Stores all of them in memory
Returns a list containing all of them

In genexp -
Only a generator object is created
Values are produced one at a time when requested
'''

import sys

lst = [x for x in range(1_000_000)]
gen = (x for x in range(1_000_000))

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))

# when we do list(gen) then the values are produced and stored
store = list(gen)
print(sys.getsizeof(store))