#! /usr/bin/python3

# --- Battery included modules -------------------------------------------
import sys
import unittest as ut

# --- Locally installed modules -----------------------------------------
# --- Program internal modules -------------------------------------------
# ------------------------------------------------------------------------

import numpy as np
import matplotlib as plt
import click

@click.command()
@click.option('--name', prompt='Your name please', help='Enter your name here.')
def main(name):
   print(name + 'calculator') 

if __name__ == '__main__':
    sys.exit(0)

class Tests (ut.TestCase):

    def setup(self):
        number_one = 4
        number_two = 2

    def the_calculator_could_add(self,number,number):
        self.assertEqual(self, number,number,msg='HolyCrap')

    def the_calculator_could_subtract(self):
        pass
