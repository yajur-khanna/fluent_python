# Without list comprehension
symbols = "@#$!"
unix = []
for symbol in symbols:
    unix.append(ord(symbol))
print(unix)

# With list comprehension
unix = [ord(symbol) for symbol in symbols]
print(unix) # More readable, faster, definitive goal

# list comprehension ignores line breaks hence we can implement nested loops in same line
symbol_and_unix = [[symbol, i] for symbol in symbols for i in unix]
print(symbol_and_unix) # all permutations of symbols above and their ords


# Walrus operator :=

x = [1, 2, 3, 4]
sq = [a**2 for a in x]
print(sq)
try:
    print(a) # type: ignore
except Exception as NameError:
    print("'a' is not defined outside of list comprehension")

# with walrus operator we can define a variable in list comprehension that exists outside of it

sq = [b := a**2 for a in x]
print(sq)
print(b) # the last iteration of the for loop assigned 4**2 = 16 to be, so b holds value 16



# Listcomps vs maps and filter

symbols = "$&#@{!"
lc = [ord(symbol) for symbol in symbols if ord(symbol) > 60]
print(lc)

# map and filter
mf = list(filter(lambda c: c>60, map(ord, symbols)))
print(mf)

# map - Take each item in the iterable, apply the function to it, and give me the results
# map returns a lazy iterator to the result of the function
nums = [1, 2, 3]
result = map(lambda x: x * 2, nums)
# at this point no multiplication has happened and result is not stored
# because map returns lazy iterator, calculates only when called

print(result) # map stores like an iterator; 2 with next() which stores 4...
# 2 -> 4 -> 6

print(next(result))  # 2
print(next(result))  # 4
print(next(result))  # 6

# if we convert back to list the list will be empty as the iterator has been exhausted
print(list(result))

# filter is just like map but performs bool operation (true or false)
# filter just returns a lazy iterator to values which the functions returns true for
a = list(filter(lambda c: c>60, [1, 2, 43, 80, 100]))
print(a)

# nested list -

lst = [[]] * 2
print(id(lst[0]))
print(id(lst[1]))
# this creates copies of the same object, both nested lists at index 0 and 1 hold reference
# to the same list object

lst = [[], []] # or lst = [list(), list()]
print(id(lst[0]))
print(id(lst[1]))
# now both nested list point to 2 different list objects

lst = [[] for i in range(5)]
for i in range(5):
    print(f"ID {i+1} ", id(lst[i]))


# Iterating a list of tuples -
b = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
print("Iterating list of tuples -")
for i, j in b:
    print(i, j)