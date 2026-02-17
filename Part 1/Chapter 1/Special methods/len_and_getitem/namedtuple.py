import collections

# Classs objects

class Yajur:
    first_name = 'Yajur'
    last_name = 'Khanna'
    def printname(self):
        return f"{self.first_name}" + " " + f"{self.last_name}"

me = Yajur()
print(me.printname())

# Here a class with name Yajur was created, and it is also stored in a variable named 'Yajur'
# both class name and the variable that stores the class object are the same


# namedtuple - initializes subclass of tuple with attributes defined in second parameter

sample = collections.namedtuple('sample_class', ['x', 'y'])

'''This creates a class that inherits from the class 'tuple'. Here the class
created has the name 'sample_class' but the variable that stores the class is named 'sample'
When we create an instance of a class we use the variable that stores the class to init
not the class name'''

s = sample(1, 2)

'''
class Sample(tuple):
    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]
'''

# we can use the attribute name to retrieve the value stored by the attribute
print(s.x)

# Since namedtuple inherits tuple, it is also immutable
try:
    s.x = 100
except Exception as AttributeError:
    print("Cannot re-assign value in a tuple")


# we can also retrieve values like a normal tuple
first_val, sec_val = s # s is a tuple
print(f"Fist Value in tuple: {first_val}"+"\n"+f"Second Value in tuple: {sec_val}")

# s is object of class 'sample_class'
print(s)

print(type(s))

print(isinstance(s, sample)) # s is object of class 'sample_class'

print(isinstance(s, tuple)) # s is also an object of class 'tuple' as 'sample_class'
# inherits 'tuple'