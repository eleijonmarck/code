#!/usr/bin/python3

import sys
import database

def read_all_movies():
    return print(database.readall())

def add_a_movie():
    title = input("what title is the movie")
    description = input("describe what the movie is about")
    likes = int(input("how do you like it from one to 10"))
    database.add_movie(title,description,likes)
    return print("Movie %s added to the collection" % (title))

switcher = { 
        '0': read_all_movies,
        '1': add_a_movie }
def main():
    print("Welcome to the movie application")
    menu()

def menu():
    print("Please choose a option below")
    for key in switcher.keys():
        print(key)
    option = input("Please type in your option: ")
    if option in switcher:
        choosed_option(option)
        menu()
    else:
        print("Ohhhh sorry but it seems that you did not write the corrrrect option")

def choosed_option(option):
    func =  switcher.get(option, lambda: "nothing")
    return func()


if __name__ == "__main__":
    main()
