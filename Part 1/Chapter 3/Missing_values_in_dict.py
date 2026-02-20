# Storing word locations in a txt file using dict -
import re
import sys

WORD_RE = re.compile(r'\w+')

index = {}
with open("zenofpython.txt", encoding='utf-8') as f:
    for lineno, line in enumerate(f, 1): #(f, 1) => start counting lines with 1 indexing
        for i in WORD_RE.finditer(line): # finditer returns matches as defined by WORD_RE
            word = i.group() # return entire match
            '''
            text = "Price: $45"
            pattern = re.compile(r"\$(\d+)")
            m = pattern.search(text)

            What regex does -
            \$      → match $
            (\d+)   → capture digits

            m.group(0)   # '$45'   → entire match
            m.group(1)   # '45'    → first sub-expression (\d+)
            '''
            column_no = i.start() + 1 # start() returns starting position of word in 0 index
            location = (lineno, column_no)
            occurences = index.get(word, []) # returns [] if first occurence of word
            occurences.append(location)
            index[word] = occurences
    for word in sorted(index, key=str.upper):
        '''
        "a"        → "A"
        "Although" → "ALTHOUGH"
        key=str.upper tells sorted to compare uppercase version of str for sorting
        '''
        print(word, index[word])


# We can simplify this code using setdefault() -
index = {}
with open("zenofpython.txt", encoding='utf-8') as f:
    for lineno, line in enumerate(f, 1):
        for i in WORD_RE.finditer(line):
            word = i.group()
            column_no = i.start() + 1
            location = (lineno, column_no)
            index.setdefault(word, []).append(location)
    print("\nOuput with setdefault -")
    for word in sorted(index, key=str.upper):
        print(word, index[word])

'''
index.setdefault(word, []).append(location) this is equivalent to -
if key not in my_dict:
    my_dict[key] =  []
my_dict[key].append(new_value)
Except setdefault() will do it in one search call while the code block below will take 2 calls
'''


# Handling missing keys in dict -

# Using defaultdict -
from collections import defaultdict

'''Whenever we call my_dict[non-existent-key], what defaultdict does -
calls list() to create a new list, inserts that list into my_dict using 'non-existent-key'
as key, and then returns a reference to that list
'''

# same word position example using defaultdict -
index = defaultdict(list) # sets default values to list type
with open("zenofpython.txt", encoding='utf-8') as f:
    for lineno, line in enumerate(f, 1):
        for i in WORD_RE.finditer(line):
            word = i.group()
            column_no = i.start() + 1
            location = (lineno, column_no)
            index[word].append(location)
    print("\nOuput with defaultdict -")
    for word in sorted(index, key=str.upper):
        print(word, index[word])

# Important - defaultdict[non-existent-key] will create new empty value of defined datatype
# but defaultdict.get(non-existent-key) will still return None


# __missing__ -

# This is the method that handles missing values in defaultdict
# StrKeyDict0 (custom defined subclass of dict) example -

# This subclass dict returns str value for any key search, for example -
class StrKeyDict0(dict):

    # If __missing__ is called it means key 'key' wasn't found
    def __missing__(self, key):
        if isinstance(key, str): # if the key trying to be searched is a str
            raise KeyError(key) # we raise error since key being searched is already a str
        return self[str(key)] # if its not str we convert it to str and return
    '''
    self is a dict class so self[] is just my_dict[key]
    so essentially we convert non-str type to str and perform __getitem__ again
    '''
    def get(self, key, default=None):
        try:
            return self[key] # Triggers __getitem__ may try __missing__
        except KeyError:
            return default # this is the default value returned in .get(x, default)
    '''
    get() in dict does not call __missing__ so we define a 
    get() in our custom class to override the dict get() method, so that
    our custom get() calls __missing__ when a key value is not found

    get() or my_dict[key] calls __getitem__ which does -
    if key in dict:
       return value
    else:
        if __missing__ exists:
            call __missing__(key)
        else:
            raise KeyError
    so return self[key] in our defined get() is running this code by calling __getitem__
    '''
    def __contains__(self, key): # handles 'in' like key in my_dict -> returns true/false
        # key in self.keys() -> '2' in strdict{'2': 'two'} -> returns Tue
        # str(key) in self.keys() -> 2 in strdict{'2': 'two'} -> fallsbacks __missing__
        # still returns True
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2']) # '2' is already in dict as a key
print(d[4]) # 4 is not a key ('4' is), so __missing__ is called and '4' is converted to '4'
# and '4' value ('four') is returned
print(d[1]) # 1 does not exist so __missing__ is called which converts it to '1' and
# __getitem__('1') is called which also does not exist as key so KeyError is raised