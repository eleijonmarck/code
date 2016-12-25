import csv
import numpy as np

"""
1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD

You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with 5.

So, in this example, the bathroom code is 1985.
"""

def find_bathroom_code():
    bathroom_codes = read_the_bathroom_codes()


def create_keypad_grid():
    grid_matrix = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
    lol_grid = [[1,2,3],[4,5,6],[7,8,9]]
    return lol_grid

def read_the_bathroom_codes():
    filename = "bathroom_codes.txt"
    with open(filename) as csv:
        bathroom_codes = csv.readlines(filename)

    return bathroom_codes

def test_1():
	code = []
	instructions = [['ULL'],['RRDDD'],['LURDL'],['UUUUD']]
	keypad = create_keypad_grid()

if __name__ == '__main__':
	test_1()
	find_bathroom_code()
