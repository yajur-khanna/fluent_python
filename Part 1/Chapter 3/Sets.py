# The most obvious use case of set it to store only unique elements- remove duplicacy

l = set(['spam', 'ham', 'spam', 'egg', 'ham', 'spam', 'egg'])
print(l) # SETS DO NOT preserve order of insertion
l.add('bam') # bam was inserted last
print(l) # bam will occur at any position in the set randomly

# even if we convert set back to list, we will only get unique items
print(list(l))
# If we want to remove duplicates but also preserve the order of insertion, we can use dicts

# Set elements must be hashable
b = 'a'
a = set(set(b)) # this is converting a datatype set to datatype set itself
print(a)

try:
    b = {{'a'}}
    print(b)
except TypeError:
    print("Sets are not hashable so you cant build nested sets")
    # for something to be inside a set it must be hashable, but sets are not hashable
    # so we cannot put a set inside a set. However, frozensets are hashable, so we can
    # put a frozen set inside a set

# sets support operations from set theory like -
'''
1. | ; Union
2. & ; Intersection
3. - ; difference (elements in A that are NOT in B)
4. <= ; is subset
5. >= ; is superset
'''


# To initialize an empty set we need to use -
a = set() # initializes empty set
print(a)
b = {} # this initializes empty dict
print(b)
c= {1, 2, 3} # this intializes a filled set
print(type(c))
d = {1: 'a', 2: 'b', 3: 'c'} # initializes filled dict
print(type(d))

# frozen set however must be initialized by calling the constructor - frozenset()


# setcomp -

from unicodedata import name
sc = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
# chr(36) = $, name($) = 'DOLLAR SIGN', if chr has no name '' is returned
print(sc)

'''Adding elements to set may change the order of existing elements as seen above, this
is because when the hashtable is more than 2/3 full, Python needs to resize the table
and when this happens elementss are reinserted and their relative ordering changes'''

# We do not need two sets to perform set theory operations, we can do it with one set
# and one collection object as well
io = {1: 'a', 2: 'b', 4: 'c', 6: 'c', 7: 'd'}
io2 = [1]
s = {1, 2, 7}
print(a.union(io), a.union(io2)) # | doesn't work here

# for removing elements from set we can use discard(element)
s.discard(7)
print(s)
s.discard(8) # if element is not present and we discard it, discard() will not raise error
print(s)

# However if we use remove(element) and the element is not present, it will raise KeyError
try:
    s.remove(8)
except KeyError:
    print('8 is not in the set, use discard to not raise error while removing doubtful elements')

# dict_keys and dict_items also support set operations -
d1 = dict(a=1, b=2)
d2 = dict(b=20, c=40)
print(d1.keys() & d2.keys()) # returns a set

# They are also compatible with sets
s1 = {'a', 'b'}
print(d1.keys() & s1) # returns a set

print(d1.keys() | s)

# Atttempting set operations on dict_items with unhashable values will return TypeError
# on the other hand dict_keys can always be used as sets, because keys by definition are
# hashable