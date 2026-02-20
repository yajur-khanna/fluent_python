# dictcomp -

dial_codes = [(880, 'Bangladesh'), (55, 'Brazil'), (86, 'China'), (234, 'Nigeria')]
dc = {country: code for country, code in dial_codes}
print(dc)

dc_upper = {code: country.upper() for code, country in sorted(dial_codes) if code < 100}
print(dc_upper)


# unpacking mappings -

# dict unpacking - **{x: 1} <=> x = 1

def dump(**kwargs):
    return kwargs # key word arguments

print(dump(**{'x': 1}, y=2, **{'z': 3}))
'''
**{'x': 1} unpacks to x=1
Then inside dump() we pass x=1 with ** prefixed
which converts back to {'x': 1}
'''

# This works when keys are strings and unique, becuase duplicate keyword arguments
# are not allowed, f(x) if you pass both x=1 and x=2 error is raised
d = {'a':0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}
print(d) # latest x value will be stored for key 'x'


# dict merge
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d3 = {'b': 5}
print(d1 | d2 | d3) # | is dict merge operator => creates new dict with all keys from all dict
# if keys overlap right-side wins and its value is inserted in the new dict


# dict in-place update
d1 |= d2
print(d1)


# Pattern matching with mappings -

def get_creator(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}: # names is a seq datatype
            # *names is equivalent to names = list(sequence)
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record}")
        
b1 = dict(api=1, author='Dougles Hofstadter', type='book', title='Godel, Escher, Bach')
print(get_creator(b1))


# ordered dict -
from collections import OrderedDict
b2 = OrderedDict(api=2, type='book', title='Python in a nutshell', authors='Martelli Ravenscroft Holden'.split())
print(get_creator(b2))
        
# While order of insertion is preserved in dict as well as OrderedDict
od1, od2 = OrderedDict(a=1, b=2), OrderedDict(a=2, b=1)
d1, d2 = dict(b=1, a=2), dict(a=2, b=1)
print(od1==od2) # False for ordered dict
print(d1==d2)

# Also ordered dicts support popitem(last=False) and hence FIFO and LIFO behavior,
# dict's popitem() does not have the last key word arg

food = dict(category='ice cream', flavor='vanilla', price=99)
match food:
    case {'category': 'ice cream', **details}:
        print(f"Ice cream details: {details}")


# Shallow vs deep copy

import copy

# shallow copy -
d1 = {
    "name": "Yajur",
    "scores": [90, 95]
}

d2 = d1.copy()

# d1 and d2 have different references but "name" and "score" in d1 and d2 have the same
# reference

d2["scores"].append(100)

print("d1: ", d1)

d3 = copy.deepcopy(d1)

d3["scores"].remove(90)
print("d3: ", d3)
print("d1: ", d1)


# dict has popitem() as well used to remove last inserted item
popped = d3.popitem()
print(popped) # d3 scores will be returned, scores was last 'item' added to dict

