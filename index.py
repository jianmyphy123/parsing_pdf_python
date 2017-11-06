from math import pi
import math


class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = ""

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name
    def set_height(self, height):
        self.__height = height
    def set_weight(self, weight):
        self.__weight = weight
    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name
    def get_height(self):
        return self.__height
    def get_weight(self):
        return self.__weight
    def get_sound(self):
        return self.__sound

    def get_type(self):
        print('Animal')

    def toString(self):
        return "{} is {} cm tall and {} killograms and say {}".format(self.__name,
                                                                        self.__height,
                                                                        self.__weight,
                                                                        self.__sound)

class Dog(Animal):

    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

        # Animal.__init__(self, name, height, weight, sound)
    def set_owner(self, owner):
        self.__owner = owner
    def get_owner(self):
        return self.__owner
    def get_type(self):
        print('Dog')

    def toString(self):
        return "{} is {} cm tall and {} killograms and say {}. His owner is {}".format(self.get_name(),
                                                                                        self.get_height(),
                                                                                        self.get_weight(),
                                                                                        self.get_sound(),
                                                                                        self.__owner)

    def multiple_sounds(self, how_many = None):
        if(how_many is None):
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()



cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())
# Whiskers is 33 cm tall and 10 killograms and say Meow

spot = Dog('Spot', 53, 27, 'Ruff', 'Derek')
print(spot.toString())
# Spot is 53 cm tall and 27 killograms and say Ruff. His owner is Derek

test_animals = AnimalTesting()
test_animals.get_type(cat)
# Animal
test_animals.get_type(spot)
# Dog
spot.multiple_sounds(4)
# RuffRuffRuffRuff
spot.multiple_sounds()
# Ruff






# list
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares2 = [x**2 for x in range(10)]
print(squares2)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

listval = [(x, y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(listval)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([fruit.strip() for fruit in freshfruit])
# ['banana', 'loganberry', 'passion fruit']

print([str(round(pi, i)) for i in range(1,6)])
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']









# nested list
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]











# tuple
t = 1,2,3,4,5;
t2 = t, (1,2,3,4,5)
print(t2);
# ((1, 2, 3, 4, 5), (1, 2, 3, 4, 5))

t = 1,2,3
x, y, z = t
print(x, y, z)
# 1 2 3











# set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# {'apple', 'banana', 'pear', 'orange'}

print('orange' in basket)
# True

a = set('abracadabra')
print(a)
# {'a', 'd', 'b', 'r', 'c'}
b = set('alacazam')
print(a-b)
# {'b', 'r', 'd'}

print({ x for x in 'abracadabra' if x not in 'abc'})
# {'d', 'r'}










# dict
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
# {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(list(tel.keys()))
# ['jack', 'sape', 'guido']
print(tuple(tel.values()))
# (4098, 4139, 4127)
print(list(tel.items()))
# [('jack', 4098), ('sape', 4139), ('guido', 4127)]
a = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(a)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
print({x: x**2 for x in (2,4,6)})
# {2: 4, 4: 16, 6: 36}
print(dict(sape=4139, guido=4127, jack=4098))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}







# looping
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# gallahad the pure
# robin the brave
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}'.format(q, a))
# What is your name? It is lancelot
# What is your quest? It is the holy grail
# What is your favorite color? It is blue
for i in reversed(range(1, 10, 2)):
    print(i, ' ', end="")
print()
# 9  7  5  3  1
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f, ' ', end="")
print()
# apple  banana  orange  pear
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
# [56.2, 51.7, 55.3, 52.5, 47.8]

















from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

import pandas as pd
import numpy as np

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()

    output.close
    return text


text = convert('./data/MR_CH_en_CH0226976816_YES_2017-09-30.pdf', [1])
textArr = text.split('\n')

indexArr = np.where(textArr=='')
print(indexArr[0][0], indexArr[0][1], indexArr[0][2])

df = pd.DataFrame({'title': textArr[1:indexArr[0][0]], 'value': textArr[indexArr[0][1]+1:indexArr[0][2]]})
print(df)

df.to_csv('output/csvfile.csv', sep=',', index=False, header=False)
df.to_excel('output/excelfile.xlsx', sheet_name='sheet1', index=False, header=False)
