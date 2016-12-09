import numpy
import csv
import pandas 

class elf:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.moves_made = [[x,y]]
        self.uniq_moves = []
        self.seen_moves = []
        self.first_seen_move = 0

    def move(self,gen):
        move = gen.next()
        if move[0] == 'L':
            self.direction = (self.direction - 1) % 4
        else:
            self.direction = (self.direction + 1) % 4

        self.step(int(move[1:]))

    def step(self, steps):
        if self.direction == 0:
            for step in range(1,steps + 1):
                self.have_i_visited_this_before([self.x, self.y + step])
            self.y += steps

        if self.direction == 1:
            for step in range(1,steps + 1):
                self.have_i_visited_this_before([self.x + step,self.y])
            self.x += steps

        if self.direction == 2:
            for step in range(1,steps + 1):
                self.have_i_visited_this_before([self.x , self.y - step])
            self.y -= steps

        if self.direction == 3:
            for step in range(1,steps + 1):
                self.have_i_visited_this_before([self.x - step,self.y])
            self.x -= steps

    def have_i_visited_this_before(self, pos):
        if (pos in self.seen_moves) & (self.first_seen_move == 0):
            self.seen_move = pos
            self.first_seen_move = 1
        if pos not in self.seen_moves:
            self.uniq_moves.append(pos)
            self.seen_moves.append(pos)

    def print_elf(self):
        print(self.x,self.y,self.direction, self.seen_moves)

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

    gen = move_parser(moves)
    for i in range(len(moves)):
        elfy.move(gen)

        if (elfy.have_i_visited_this_before(i)):
            print("I've visited this before!, Blocks away %s ",
            count_distance(elfy))
            return 0

    elfy.print_elf()
    print("distance to the hq: %s",count_distance(elfy))
    print("distance to the first seen brick is : %s",
            abs(elfy.seen_move[0]) + abs(elfy.seen_move[1])) 

main()
