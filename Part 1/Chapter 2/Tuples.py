import os

# tuples unpacking -

# parallel assignment -
lax_coords = (33.87575, -112.4874) # position matters when using tuples as records
lat, long = lax_coords
print(lat, long)
# we can easily swap values -
long, lat = lat, long
print(lat, long)


city, year, pop, chg, area = ('Boston', '2026', "2M", 0.67, "02119")
print(year)

traveler_ids = [('BRA', '313393'), ('US', '119882'), ('ESP', '19893'), ('ESP', '123484')]
# tuple sorts by giving first preference to first element (unless coded otherwise), if first
# element is equal is checks the second element and so on
for passport in sorted(traveler_ids):
    # % unpacks tuple
    print('%s/%s' % passport)
    '''
    %s %s -> two placeholders
    we have a tuple with two values so python assigns first value to first %s
    and second value to second %s
    %d for int, float
    '''


# Immutability in tuples -

a = ('10', 'alpha', ['1', '2'])
b = ('10', 'alpha', ['1', '2'])
print(a == b)

b[-1].append('99')
print(a == b)

# Tuples hold references to the objects in them, tuple immutability means we cannot
# change the reference to the object but we can change the object. This is why
# tuples 'a' and 'b' are not equal when we append 99 at the end of 'b'
# b = b = ('10', 'alpha', ['1', '2', '99'])

tf = ('10', 'alpha', ('1', '2'))
tm = ('10', 'alpha', ['1', '2'])

# We can check mutability of any object using built-in function hash()

def fixed(o):
    try:
        hash(o)
    except TypeError:
        print('Error')

fixed(tf) # tf returns true as it contains references to all immutable objects
# strings are immutable as if we add char to str it is stored in new memory loc
# the original str cannot be altered directly, same goes for int
fixed(tm)


# os.path.split() uses tuples
filename = os.path.split('/Users/yajur/Fluent Python/Part 1/Chapter 1/Implementing_vectors.py')
print(filename)


# using * to grab excess items -
a, b, *rest = range(5)
print("a: ", a, ", b: ", b, ", rest: ", rest)

# in parallel assignment * can be applied to only 1 variable but at any position -
a, *rest, c, d = range(5)
print("a: ", a, ", rest: ", rest, ", c: ", c, ", d: ", d)

# in function calls we can use * multiple times -
def fun(a, b, *rest):
    return a, b, rest

print(fun(1, 2, 3, 4, 5)) # (1, 2, (3, 4, 5))
print(fun(*[1, 2], 3, *range(4, 7))) # *[1, 2] -> expand [1, 2] as 1, 2
# *range(4, 7) -> expand range(4, 7) -> 4, 5, 6
# after expansion input becomes - 1, 2, 3, 4, 5, 6
# a is mapped to 1 and b to 2, rest contains (3, 4, 5, 6)

a = [*range(4), 4]
print(a) # [0, 1, 2, 3, 4]

b = {*range(4, 8), 1, 2, *range(8, 12)}
print(b)


# Single item tuples must have trailing commas -
a = (5)
print(type(a))

a = (5, )
print(type(a))