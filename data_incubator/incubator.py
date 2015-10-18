#!/usr/bin/python -tt

import sys
#import time
import math
from random import shuffle
from itertools import permutations
import numpy as np

def main():

    # get sequence length and number of shuffle iterations
    # if N < 10 try all permutations. For larger N randomly
    # shuffle the links NUM_ITERS times
    N = int(sys.argv[1])
    if len(sys.argv) == 3:
        NUM_ITERS = int(sys.argv[2])
    else:
        NUM_ITERS = 1000

    # initialize links array
    links = np.arange(N)

    avgM = 0
    var = 0
    # compute with all permutations
    if N < 9:
        perm = permutations(links)
        while True:
            try:
                links = perm.next()
                #print links
                M = 1
                for i in range(1,N):
                    if sum(abs(links[:i]-links[i]) == 1) == 0:
                        M+=1
                avgM += M
                var += M*M 
            except StopIteration:
                break
        
        avgM = float(avgM)/math.factorial(N)
        var = float(var)/math.factorial(N)# - avgM*avgM
        std = math.sqrt(var)

    # shuffle links NUM_ITERS times
    else:
        shuffle(links)    
        iter = 0
        while iter < NUM_ITERS:
            M = 1
            for i in range(1,N):
                if sum(abs(links[:i]-links[i]) == 1) == 0:
                    M += 1
            avgM += M
            var += M*M
            iter += 1
            shuffle(links)
        
        avgM = float(avgM)/NUM_ITERS
        var = float(var)/NUM_ITERS - avgM*avgM
        std = math.sqrt(var)
    
    print 'average M: ', avgM
    print 'std: ' , var

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
