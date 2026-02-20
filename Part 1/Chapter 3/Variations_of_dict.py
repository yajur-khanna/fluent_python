from collections import ChainMap

d1, d2 = dict(a=1, b=3), dict(a=2, b=4, c=6)
# keyword syntax for initializing dicts means the key will be stored as str
# we cannot initialize dict(30='b')
cm = ChainMap(d1, d2)
print(cm['a'])

# ChainMap hold references to input mappings, so update in cm would affect d1 and d2
cm['c'] = -1
print(d1, d2) # d1 is affected as assignment always goes to first mapping in ChainMap

from collections import Counter

# counter is used to maintain integer count for each key, updating an existing key adds to
# its count as opposed to dict in which the value is replaced by the new value
c = Counter({'a': 5, 'b': 2, 'c': 3, 'r': 1, 'd': 4})
c.update('aaaaazzz')

print(c)
print(c.most_common(3))


import shelve

# shelve.Shelf is a dict stored on disk, we use it when we want dict like behavior but
# the data should survive after the program terminate

with shelve.open('data2') as db:
    db['a'] = [1, 2, 3] # stores data on disk as .db

with shelve.open('data') as db:
    print(db['a']) # 'db' functions like dict

# A shelf instance is a context manager so using 'with' closes it after use
'''
A context manager is an object that defines what should happen before and after
a block of code runs

with context manager (implements special methods __enter__ and __exit__) -
with open("file.txt") as f:
    data = f.read()

without context manager -
f = open("file.txt")
data = f.read()
f.close()
'''


# UserDict -
from collections import UserDict

'''We can implement customdict classes like StrKeyDict0 (from Missing_values_in_dict.py)
better using UserDict. This is because when we inherit from built-in dict many methods
that we define are bypassed by some in-built dict methods. For examaple -
'''
class MyDict(dict):
    def __missing__(self, key):
        print("__missing__ called for", key)
        return "default value"

d = MyDict()

print("d['x'] = ", d["x"])     # triggers __missing__
print("d.get('x') = ", d.get("x"))  # bypasses __missing__

class MyUserDict(UserDict):
    def __missing__(self, key):
        print("__missing__ called for ", key)
        return "default value"
    
ud = MyUserDict()
print("d['x'] = ", ud["x"])     # triggers __missing__
print("d.get('x') = ", ud.get("x"))  # doesn't bypass our __missing__ method


# We can define a better strdict using UserDict -

class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise ValueError
        return self[str(key)]
    def __contains__(self, key):
        return str(key) in self.data
    '''
    UserDict has an internal instance of dict called data where actual items are held
    using self.data simplifies implementation as opposed to invoking self.keys()
    '''
    def __setitem__(self, key, item):
        self.data[str(key)] = item
    # because setitem converts keys to str, we can assume all keys stored in StrKeyDict
    # are str type
    '''
    Here we are overidding UserDict.__setitem__ with out __setitem__, where if we used
    dict the dict then some dict operations may bypass our __setitem__
    '''


# Immutable mappings -

'''There are no explicity immutable mappings but the types module provides a class
called MappingProxyTypre, where given a mapping it returns a proxymapping, i.e.
it is read only version of the original mapping, reflecting changes in the original
mapping but not allowing original mapping to be changed through it'''

from types import MappingProxyType

d = {1: 'A'}
mpt = MappingProxyType(d)
print(mpt)
try:
    mpt.update({2: 'B'})
    print(mpt)
except Exception as KeyError:
    print("Cannot make changes to a proxy dict")
d[2] = 'B'
print(d) # Can still change original dict but not it's proxy and changes will be reflected
# in proxy
print(mpt)


# Dictionary views -

d = dict(a=10, b=20, c=30)
values, keys, items = d.values(), d.keys(), d.items()
print(f"values: {values}, keys: {keys}, items: {items}")
print("Length of values: ", len(values))
print(list(keys))
print(reversed(items)) # returns a custom iterator pointing to last element
print(next(reversed(items))) # calling iterator returns last element
# now iterator is pointing to second last element

'''values, keys and items variables return instances of dict_values, dict_keys, and dict_items
classes. These are read-only, i.e. we can see changes made to original dict but not
make changes to it through these classes. Which makes sense as when we update a dict
and call .items() we get the updated list of items'''


# Some practical consequences of how dicts work under the hood -
'''1. Keys must be hashable, i.e., implement __hash__ and __eq__
2. Hash tables are the data structure that power dicts
3. Key ordering is preserved
'''