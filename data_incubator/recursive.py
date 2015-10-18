#!/usr/bin/python -tt

import sys
import time
import math
import numpy as np

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_momo(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():
    tic = time.clock()
    fib(30)
    toc = time.clock()
    print toc-tic
    
    use Memoize;
    memoize('fib')
    tic = time.clock()
    fib(30)
    toc = time.clock()
    print toc-tic
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
