#!/usr/bin/env python2


#use the ctrl+p and ctrl+n

import fileinput
import numpy as np


#input:
#first line: n, m where n is the #lights/switches, m is #photos

#concecutive lines: each photo is described by 2 lines, 
#each line containing a binary string of len n (#lights)

def main():


	x = [0,1,2]
	filelist = [map(lambda x: './apparatus-sample-data/apparatus.0' + str(x) + '.in',x)]
	print filelist
	
	for line in fileinput.input(filelist):
		print line

		fileinput.close()


main()
