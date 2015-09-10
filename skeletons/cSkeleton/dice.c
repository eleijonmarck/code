// -*- C -*-

#include <stdio.h>

//#include <rand.h>

//////////////////////////////////////////////////////////////////////
typedef struct dice{
  char player [24];
  int score;
} dice_t;

//////////////////////////////////////////////////////////////////////

static int rollDice(*dice dice) {
  dice.score = rand(10);
}


int main() {
  printf("Welcome to the dice program!");
  int score = rollDice(dice);
  printf(score,%i);
}


