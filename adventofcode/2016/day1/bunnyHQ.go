package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

type position struct {
	x, y int
}

var direction = []position{
	{0, 1},
	{1, 0},
	{0, -1},
	{-1, 0},
}

func distance(pos position) int {
	return pos.x + pos.y
}

func parse(s string) (int, int, error) {
	var direction, dist int

	if len(s) < 2 {
		err := fmt.Errorf("invalid instructions %q", s)
		return 0, 0, err
	}
	if s[0] == 'L' {
		direction = -1
	} else if s[0] == 'R' {
		direction = 1
	} else {
		err := fmt.Errorf("invalid direction %q", s)
		return 0, 0, err
	}

	dist, err := strconv.Atoi(s[1:])
	if err != nil {
		return 0, 0, err
	}
	if dist < 0 {
		err := fmt.Errorf("invalid distance %q", s)
		return 0, 0, err
	}
	return direction, dist, err
}

func move(in string) (int, int, error) {
	var currentDirection int
	var dist2 int
	var pos position
	var found2 bool

	visited := make(map[position]int)
	dirs := strings.Split(in, ", ")

	for _, v := range dirs {
		dir, dist, err := parse(v)
		if err != nil {
			return 0, 0, err
		}

		currentDirection = (currentDirection + dir + 4) % 4

		for i := 0; i < dist; i++ {
			pos.x += direction[currentDirection].x
			pos.y += direction[currentDirection].y

			visited[pos]++

			if !found2 && visited[pos] > 1 {
				dist2 = distance(pos)
				found2 = true
			}
		}
	}
	fulldist := distance(pos)

	return fulldist, dist2, nil
}

func main() {
	filename := "input.txt"
	instructions, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Fprintln(os.Stderr, filename)
	}

	s := strings.TrimSpace(string(instructions))

	dist, dist2, err := move(s)
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
	}

	fmt.Printf("blocks : %d\nblocks2 : %d\n", dist, dist2)
}
