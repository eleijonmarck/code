import csv

def main():
    bathroom_codes = read_the_bathroom_codes()


def create_keypad_grid():
    return grid
def read_the_bathroom_codes():
    filename = "bathroom_codes.txt"
    with open(filename) as csv:
        bathroom_codes = csv.readlines(filename)

    return bathroom_codes

