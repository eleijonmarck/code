#!/usr/bin/env python3

# --- Battery included modules -------------------------------------------
import sys
import unittest as ut

# --- Locally installed modules -----------------------------------------
# --- Program internal modules -------------------------------------------
# ------------------------------------------------------------------------

if __name__ == '__main__':
    sys.exit(0)

class Tests (ut.TestCase): pass

#################################################################

def dataSetToFile(dataSet):


    ## POSIX ONLY ####
    paths = [line[2:] for line in subprocess.check_output("find ../.. -iname '*.csv'", shell=True).splitlines()]
    ## ########## ####

    def find(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    dataSet += '.csv'

    return find(dataSet, '../..')

#################################################################
# to preProcess inputData into how many appliances

# training for each individual source in the household
# regularization parameter penalty,
# gradient step size alpha
# convergence rate, conv
def parserData(dataSet):#, timeScale, numberAppliances):
    
    datasets = {'testhouses2012','pecan','energimynd'}

    if type(dataSet) != str:
        print 'Dataset needs to be in string format'
        sys.exit("Error message")

    if dataSet in datasets:
        readfile = dataSetToFile(dataSet)
        with open(readfile,'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter='|', quotechar='"')
            for row in reader:
                print(row['first_name'], row['last_name'])

    else:
        print 'Dataset %s does not exist in the database' %dataSet
        sys.exit("Error message")

    return houses, appliances, timeScale, gradientStep

#################################################################

