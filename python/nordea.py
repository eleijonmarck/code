#!/usr/bin/env python3

# --- Battery included modules -------------------------------------------
import sys
import unittest as ut

# --- Locally installed modules -----------------------------------------
# --- Program internal modules -------------------------------------------
# ------------------------------------------------------------------------

if __name__ == '__main__':
    sys.exit(0)

class Tests (ut.TestCase): pass


# recursive fibornacci sequence
startNumber = int(raw_input("Enter the start number here "))
endNumber = int(raw_input("Enter the end number here "))

def fib(n):
    if n < 2:
                return n
                    return fib(n-2) + fib(n-1)

                    print map(fib, range(startNumber, endNumber))
