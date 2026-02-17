from array import array

# There are 2 types of built-in sequences - containers and flat sequences

# Containers can hold different types of items and store the reference to the item object
# examples - tuples, lists, collections.deque
t = (9.46, 'dog', 8, ['me', 'you'])
print(t)
x = t[3]
y = t[3]

t[3].append("us") # tuple hold ref to list hence "us" gets appended to list in the tuple
print(t, "\n")

# id returns memory address where object lives
print("tuple[3]'s id", id(x))
print("tuple[3]'s id", id(y)) # both id's are same as t[3] hold reference to the list

print("\n")

# flat sequences hold the object itself
d = array('d', [9.34, 3.2, 1.56, 4.7, 88.3]) # 'd' is not name of subclass of array like
# namedtuple example, here 'd' tells the array class what kind of elements it stores
# d => double

x = d[3]
y = d[3]

print("array[3]'s id", id(x)) # x has different id from y, meaning they are two different objects
print("array[3]'s id", id(y)) # that have the same value


print(x is y) # is checks if these two variables pointing to the exact same object in memory


# Another way to group sequences is mutability -

# Mutable (example - list, array, collections.deque)
lst = [1, 2, 3]
lst[2] = 5
print(lst)

# Immutable (example - tuple, str, byte)
strng = "Hey"
try:
    strng[2] = "z"
except Exception as TypeError:
    print("Immutable")
