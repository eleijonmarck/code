#!/usr/bin/env python

'''
TO isntall spasm:

go to the directory of the extracted spams
run the following commands

find . -name "*.h" -print | xargs sed -i "" 's/(! isspace/(std::isspace/g'
find . -name "*.h" -print | xargs sed -i "" 's/(isspace/(std::isspace/g'
find . -name "*.cpp" -print | xargs sed -i "" 's/(isspace/(std::isspace/g'

'''

# --- Basic installed modules --------------------------------------------
import csv
import os
import sys
import subprocess # to install on POSIX: $pip install subprocess32
# --- Locally installed modules -----------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import reader

# --- Program internal modules -------------------------------------------
# import spams
# ------------------------------------------------------------------------

# if you are writing a module and not the main program
#if __name__ == '__main__':
#    sys.exit(0)

#class Tests (ut.TestCase): pass

penalty = 0.001
penaltyTEP = 0.001
penaltyGL = 0.001

#################################################################

def frobNorm(x,A,B):
    return spnorm(x-A*B)+penalty*A.sum()

#################################################################
# calculate the norm of the input matrix

def spnorm(a):
    return np.sqrt(((a.data**2).sum()))


#################################################################
# will initiualize the matrices A,B with positive values and scale
# columns of B s.t b(j) = 1
def initialize():
    pass
    # add random positive number to A,B
    # scale columns of b(j)

#################################################################
# sparse coding with penalty (penalty) as defined by 2a

def scTraining(x,B,A,penalty):
    pass
    # A = argmin frobNorm(x-B*A)**2 + penalty sum p,q (A)
    #return A

def F(x,B,A,penalty):

    pass
#    try:
#        if aggHome != X[1,1]:
#            break
#    except ValueError:
#        print "Oops!  The input is not being correctly calculated.  Try again..."
#
#    # A = argmin frobNorm(x-B*A)**2 + penalty sum p,q (A)
#    return A

#################################################################

def main():

    # if class
    # reader = reader()
    nothing = reader.parserData('testhouses2012')
    #appliances, regularizationParameter, gradientStep = parserData()
    X = np.eye(100,100)
    A = np.random.random((100,100))
    B = np.random.random((100,100))

    print A,B #spams.calcXAt(X,A)
'''
    extensions = raw_input('Please specify which extension by tep or gl')
    
    A, B = initialize()
'''
#################################################################
#################################################################
# sparse coding pre-training
'''
#use nested while loop
#while expression:
#   while expression:
#      statement(s)
#   statement(s)

    conv = 0.0001
    while 
    for i in appliance:

        A(i) = scTraining(x,B(i),A,penalty)
        B(i) = frobNorm(x,B,A(i))
'''
#################################################################
#################################################################
# discriminiative disaggregatino trainign
'''

    Astar = A, Btilde = B

# use nested loop
    conv = 0.0001
    while 
    for i in appliances:

        Ahat = F(x,Btilde,A,penalty)
        Btilde = gradiantDescent(x,Btilde,Ahat,Astar,alpha)

        for i in appliances:
            for j in houses:

                b(i,j) = b(i,j)/norm(b(i,j))
'''

#################################################################
#################################################################
'''
# energy discriminating with test data
    AhatPred = F(x,Btilde,A)

# predicting
    
    for i in appliances:
        x(i) = B(i)*Ahat
        '''
main()
