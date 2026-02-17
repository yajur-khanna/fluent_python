import math

class twoD_vector:

    def __init__(self, x_coord, y_coord):

        self.x_coord = x_coord
        self.y_coord = y_coord

    
    '''When you don’t define __repr__ (or __str__),
    Python falls back to the default representation inherited from object
    <__main__.twoD_vector object at 0x10f3a9c70>
    '''
    def __repr__(self):
        return f"twoD_vector({self.x_coord}, {self.y_coord})"
    # Note __repr__ is used for debugging and logging (developer)
    # while __str__ is used for displaying (end-user)

    # Operator methods follow argument style (self, other)
    def __add__(self, other):
        if not isinstance(other, twoD_vector):
            return NotImplemented
        rx = self.x_coord + other.x_coord
        ry = self.y_coord + other.y_coord
        return twoD_vector(rx, ry)
    
    def __mul__(self, scalar):
        if not isinstance(scalar, int|float):
            return TypeError
        rx = self.x_coord * scalar
        ry = self.y_coord * scalar
        return twoD_vector(rx, ry)
    
    def __abs__(self):
        return math.hypot(self.x_coord, self.y_coord)
    # hypot computes euclidean distancefrom origin - sqrt(x**2 = y**2)

    def __bool__(self):
        return bool(abs(self)) # bool is false for 0 and true for any numeric value
        '''
        v1 = twoD_vector(0, 0)
        v2 = twoD_vector(3, 4)

        We could also implement __bool__(self):
                                    return bool(self.x_coord or self.y_coord)
        this would return whichever value is truthy to bool
        if both are 0 i.e. false then it would return 0 to bool and bool would return False
        '''
    
vector_a = twoD_vector(2, 4)
vector_b = twoD_vector(2, 1)

print(vector_a * 3.2)
# print() calls __str__() if missing fallback is __repr__

# Truthy and falsy objects
'''
bool(x) calls __bool__ if it is not implemented then it fallsback to __len__()
if len is 0 it returns false, else true
'''

print(bool(twoD_vector(3, 4)))
print(bool(twoD_vector(0, 0)))