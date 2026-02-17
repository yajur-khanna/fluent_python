# Pythonic deck example

import collections

Cards = collections.namedtuple('Cards', ['rank', 'suit'])

class Deck:

    rank = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'Diamonds Spades Clubs Hearts'.split()

    def __init__(self):

        # Creating a list of namedtuples (all ranks and suits0)
        self._cards = [Cards(rank, suit) for suit in self.suit for rank in self.rank]

        '''
        for rank in self.rank for suit in self.suit;  is a nested loop equivalent to -

        cards = []
        for rank in self.rank:
            for suit in self.suit:
                cards.append(Cards(rank, suit))
        '''

    def __len__(self):
            return len(self._cards)
        
    def __getitem__(self, position):
            return self._cards[position]



deck = Deck()

print(deck._cards)

print(len(deck)) # without __len__ we can't directly retrive length of self._cards by
# using len(deck), it returns length of self._cards we defined it to do

print(deck[0])
'''
a = [1, 2, 3, 4]
print(a[2])

Python internally calls a.__getitem__(2)
'a' is a list object which has a __getitem__ method, whenever we pass a[index]
Python does a.__getitem__(index) and because 'a' inherits list class, python
does list.__getitem__(index)

Essentially python asks -

“Does this object implement __getitem__?”

If yes → allow obj[key]
If no → raise TypeError
'''

# Getting random cards -

from random import choice

print(choice(deck))

'''
What choice does -

Calls len(deck) → uses your __len__
Picks a random number between 0 and len(deck)-1
Calls deck[random_index] → uses your __getitem__
'''

# Because self._cards is a list, our __getitem__ automatically supports slicing
print("First 3 cards: ", deck[:3])

# Ace is stored at index 13, we can retrieve all Aces by retrieving from index 13 skipping
# next 13
print(deck[12::13])
'''
deck.__getitem__(slice(12, None, 13))
Slicing - sequence[start : stop : step]
'''

# This is why We can also iterate over the deck in any order 
for card in reversed(deck):
      print(card)

# __contains__ and 'in' operator

class myContainer:
      def __contains__(self, x):
            return x == 42 # returns true if x==42

container = myContainer()

print(24 in container) # False
print(42 in container) # True

# If a collection has no __contains__ method, 'in' does a sequential scan
print(Cards('Q', 'Hearts') in deck) # True

print(Cards('J', 'Hero') in deck) # False


# Ranking cards

suit_values = dict(Spades=3, Hearts=2, Diamonds=1, Clubs=0)
# dict(Spades=3) <=> {"Spades": 3}

def spades_high(card):
      # Deck.rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
      rank_value = Deck.rank.index(card.rank)
      # If card.rank = 3, Deck.rank.index(3) will return index value for '3'
      # from Deck.rank list, that is 1

      '''.index returns index of element in list, card.rank would return rank of card
        Deck.ranks.index('A') returns 12, if card has rank='A'
        12 is the rank value for aces'''
      return rank_value * len(suit_values) + suit_values[card.suit]

# Sorting based on our ranking defined with spades having highest value
for card in sorted(deck, key = spades_high):
      print(card)
# Lowest value card is 2 of clubs = 0 * 4 + 0 = 0, ranking starts at value 0

# For Cards('3', 'Diamonds') it returns 1 * 4 + 1 = 5, and it is ranked 6th in
# ascending order


# __iter__()

'''
for i in x; invoces __iter__(x) which returns an iterable

An iterable is any object that implements __next__() and raises StopIteation() when done
'''

class iterating:
      
    def __init__(self):
        self.obj = ['a', 3, 4.4]

a = iterating()
try:
      print(iter(a))
except Exception as TypeError:
      print("Object of type class is not iterable")



# Implementing __iter__()
class iterating:
      
    def __init__(self):
        self.obj = ['a', 3, 4.4]

    def __iter__(self):
        return iter(self.obj) # iter() is the function and it has a method __iter__()

a = iterating()
try:
      print(iter(a))
except Exception as TypeError:
      print("Object of type class is not iterable") # Now we have an iterator object
      # iter() returns this object

iterator = iter(a)

print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
     print(next(iterator))
except Exception as StopIteration:
     print("No next available")



# __init__

class Yajur:
     
     name = "Yajur"

     def print_name(self):
          return self.name

me = Yajur()
try:
     print(me.print_name())
except Exception as NameError:
     print("Object not initialized")


class Yajur:
     
     def __init__(self):
        self.name = "Yajur"

     def print_name(self):
          return self.name

me = Yajur()

try:
     print(me.print_name())
except Exception as NameError:
     print("Object not initialized")