#!/usr/bin/env python3
import unittest
import inspect

import deliverable as student
#import solution as student

class OOPTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_card(self):
        if not 'Card' in dir(student):
            self.fail('class Card does not exist')
        if not inspect.isclass(student.Card):
            self.fail('Card is not a class')

        members = dict(inspect.getmembers(student.Card))
        if members['__str__'].__qualname__.split('.')[0] != 'Card':
            self.fail('__str__ has not been overridden')
        

    def test_deck(self):
        if not 'Deck' in dir(student):
            self.fail('class Deck does not exist')
        if not inspect.isclass(student.Deck):
            self.fail('Deck is not a class')

        # Tests beyond this one assume Deck.__init__ only accepts 1 argument (self)
        sig = inspect.signature(student.Deck.__init__)
        if len(sig.parameters) != 1:
            self.fail('Expected __init__ to only accept 1 argument') 


        if not 'shuffle' in dir(student.Deck):
            self.fail('method shuffle does not exist in Deck')
        if not inspect.ismethod(student.Deck().shuffle):
            self.fail('shuffle is not a method')

        if not 'deal' in dir(student.Deck):
            self.fail('method deal does not exist in Deck')
        if not inspect.ismethod(student.Deck().deal):
            self.fail('deal is not a method')

        deck = student.Deck()
        deck.shuffle()
        self.assertEqual(len(deck.deal(5)), 5)
        
        deck = student.Deck()
        deck.shuffle()
        self.assertNotEqual(deck.deal(26),deck.deal(26))
        


if __name__ == '__main__':
    unittest.main()

