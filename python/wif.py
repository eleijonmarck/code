#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def main(a,b,c):

	#loop options

	#a = oneside
	#b = anotherside
	#c = door weight

	fit = 0
	def fit(a,b,c):

		#equation fit
		#a*sin(x)+b*cos(x) = c
		func = lambda x: c-a*np.sin(x)-b*np.cos(x)

		xInitial = 0.5
		x = np.linspace(-2,2,200)
		fit = fsolve(func, xInitial)


		plt.plot(x,func(x))
		plt.hold(True)
		plt.plot(fit, func(fit),'bo')
		plt.show()
		return fit

	fit = fit(a,b,c)

	return fit 
a = float(raw_input('What is the a-length of the object?\n'))
b = float(raw_input('What is the b-length of the object?\n'))
c = float(raw_input('What is the c-length of the object?\n'))

out = main(a,b,c)

print "Solution is x = %f " % out
