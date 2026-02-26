# 2D Vector enhanced -
import math

class Vec2:

    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __len__(self):
        return 2
    
    def __getitem__(self, i: int):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise KeyError("2 dimensional vector has only 2 coordinates (0, 1 indexing)")
        
    def __add__(self, other):
        if isinstance(other, Vec2):
            xnew = self.x + other.x
            ynew = self.y + other.y
            return Vec2(xnew, ynew)
        else:
            raise ValueError("Both vectors need to be 2 dimensional for addition")
        
    def __sub__(self, other):
        if isinstance(other, Vec2):
            xnew = self.x - other.x
            ynew = self.y - other.y
            return Vec2(xnew, ynew)
        else:
            raise ValueError("Both vectors need to be 2 dimensional for subtraction")
        
    def __mul__(self, other):
        if (isinstance(other, float)) or (isinstance(other, int)):
            xnew = self.x * other
            ynew = self.y * other
            return Vec2(xnew, ynew)
        else:
            raise ValueError("Scalar multiplication requires one scalar and one vector")
        
    def __rmul__(self, other):
        if (isinstance(other, float)) or (isinstance(other, int)):
            xnew = self.x * other
            ynew = self.y * other
            return Vec2(xnew, ynew)
        else:
            raise ValueError("Scalar multiplication requires one scalar and one vector")
        
    def __abs__(self):
        return math.sqrt((self.x**2 + self.y**2))
    
    def __bool__(self):
        return self.__abs__() == 0
    
    def __eq__(self, other):
        if len(other) == 2:
            if (other[0] == self.x) and (other[1] == self.y):
                return True
        else:
            raise ValueError("Need a 2 dimensional entity to compare with a 2D vec")
        return False
    
vec1 = Vec2(1,2)
print("Represent: ", repr(vec1))
print("Vector 1 values: ", vec1)
print("Magnitude: ", abs(vec1))
print("Multiplication with 3: ", vec1*3)
print("Reverse multiplication with 2: ", 2*vec1)
vec2 = Vec2(4,3)
print("Vector 2 values: ", vec2)
print("Vector addition: ", vec1+vec2)
print("Vector subtraction: ", vec2-vec1)
print("Check of vector: ", len(vec2))
print("x coordinate of vector 2: ", vec2[0])
print("y coordinate of vector 2: ", vec2[1])
print("Equality: ", vec1 == [1, 2])
vec3 = Vec2(0, 0)
print("Check if 0 vector for vector 3: ", bool(vec3))
print("Check if 0 vector for vector 1: ", bool(vec1))

# CardDeck -
import collections
import random

Cards = collections.namedtuple('CardsSample', ['suit', 'rank'])

class Deck:
    Rank = [i for i in range(2,11)] + list('JQKA')
    Suit = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
    def __init__(self, suit: list|None, rank:list|None, x: list[tuple]|None,):
        if x:
            self._cards = [Cards(i, j) for i, j in x]
            self._internal_dict = {(i, j): 'Yes' for i, j in x}
        elif suit and rank:
            self._cards = [Cards(i, j) for i in suit for j in rank]
            self._internal_dict = {(i, j): 'Yes' for i in suit for j in rank}
        else:
            raise KeyError("Provide valid cards for creating deck, either a list of suits and ranks or a list of tupled cards")

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, index):
        if isinstance(index, int):
            return self._cards[index]
        elif isinstance(index, slice):
            isuit, irank= [], []
            for i in range(index.start, index.stop, index.step):
                isuit.append(self._cards[i].suit)
                irank.append(self._cards[i].rank)
                res = zip(isuit, irank)
            return Deck(x=res)
        
    def __iter__(self):
        return iter(self._cards)
    
    def __reversed__(self):
        return reversed(self._cards)
    
    def __contains__(self, item: tuple|Cards):
        if isinstance(item, tuple):
            return self._internal_dict.get(item, 'No')
        x, y = Cards.suit, Cards.rank
        return self._internal_dict.get((x, y), 'No')
    
    def shuffle(self, seed=None):
        if len(self) != 52:
            return f"Cannot shuffle the deck is not full"
        if seed == None:
            for i in range(100):
                a = random.randint(0, 51)
                b = random.randint(0, 51)
                tmp = self._cards[a]
                self._cards[a] = self._cards[b]
                self._cards[b] = tmp
        else:
            rng = random.Random(seed)
            for i in range(100):
                a = rng.randint(0, 51)
                b = rng.randint(0, 51)
                tmp = self._cards[a]
                self._cards[a] = self._cards[b]
                self._cards[b] = tmp

    def __deal__(self, n):
        hand = []
        for i in range(n):
            hand.append(self._cards.pop())
        return hand
        

# Hand...