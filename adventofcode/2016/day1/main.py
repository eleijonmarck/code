import numpy
import csv
import pandas 

class elf:

    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self,gen):
        move = gen.next()
        if move[0] == 'L':
            self.direction = (self.direction -1) % 4
        else:
            self.direction = (self.direction + 1) % 4

        self.step(int(move[1]))

    def step(self, steps):
        if self.direction == 0:
            self.y += steps

        if self.direction == 1:
            self.x += steps

        if self.direction == 2:
            self.y -= steps

        if self.direction == 3:
            self.x -= steps

    def print_elf(self):
        print(self.x,self.y,self.direction)

def move_parser(moves):
    for move in moves:
        yield move.strip()

def read_moves_to_bunny_hq():
    filename = "input.txt"
    rawinput = open(filename).readline()
    return rawinput.split(',')

def count_distance(elfy):

    return abs(elfy.x) + abs(elfy.y)

def main():

    moves = read_moves_to_bunny_hq()

    elfy = elf(0,0,0)

#    testmoves = ['R2','L3']
#    gen = move_parser(testmoves)

    gen = move_parser(moves)
    for i in range(len(moves)):
        elfy.move(gen)

    elfy.print_elf()

    print("distance to the hq: %s",count_distance(elfy))

main()
