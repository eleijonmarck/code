from nose.tools import *
import unittest
from Replacer import Replacer

def setup():
    replacer = new Replacer()
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_to_replace_a_word():


class wordReplaceTests(unittest.TestCase):
    wordReplacements = ( ("företaget", "forefront"))

    def test_replacement_of_word(self):
        '''wordReplace should replace the first word with the next'''
        for badWord,goodWord in self.wordReplacements:
            result = replacer.replaceword(badWord)
            self.assertEqual(badWord,goodWord)
