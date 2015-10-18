#!/usr/bin/python -tt

import sys
import time
import math
import numpy as np

def main():
    N = int(sys.argv[1])
    K = int(sys.argv[2])
    P = list(np.random.randint(K,size=N))
    H = [0]*N
    
    C_1 = [0]*N
    for i in range(N-1):
        C_1[i] = sum(P[i+1:])
    C_1[N-1] = 0
    
    M = 0
    m = C_1[0]%K
    C_1[0] = m

    for i in range(1,N):
        H[i] = (m-(C_1[i]+M))%K
        M += H[i]
                
    print 'prisoners hats colors (white = 0, black = 1, etc...):'
    print P
    print 'prisoners\' guesses:'
    print H
    
    wrongGuesses = 0
    for i in range(0,N):
        if P[i]-H[i] != 0:
            wrongGuesses += 1
    if wrongGuesses <= 1:
        print 'success!'
    else:
        print 'failure'

      


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
