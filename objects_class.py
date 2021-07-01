#!/usr/bin/env python3
import random
'''class MyClass:
    class_attribute = 5

var = MyClass()
print(var.class_attribute)
var.class_attribute = 10

var2 = MyClass()
print(var2.class_attribute)'''

'''class Employee:

    def whatever(): #Method definition
        pass

    def __init__(self,last,first): #Special Method __init__
        self.last = last
        self.first = first

e0 = Employee('Yost', 'Nick')
print(e0.last,e0.first)'''

'''class Balloon:
    def __init__(self,altitude,weight,is_inflated):
        self.altitude = altitude
        self.weight = weight
        self.is_inflated = is_inflated

    def __str__(self):
        return 'A balloon cannot be printed you idiot'

    def ascend(self):
        self.altitude += howmuch

    def descend(self):
        self.descend -= howmuch
        if self.altitude < 0:
            self.altitude = 0'''

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.value, self.suit)'

class Deck:

    def __init__(self):
        self.card = []
        self.build()


    def shuffle(self):
    '''Randomly shuffles the deck
    Args:
        None
    Returns:
        None
    '''
    pass

    def deal(self,cards=1):
    '''Deals a number of cards
    Args:
        cards (int): the number of cards to remove from the deck
    Returns:
        List: list of cards dealt
    '''
    pass
