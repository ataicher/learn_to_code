#!/usr/bin/python -tt

import sys
import time

def make_change(n,d):
  if d == 25:
    n_d = 10
  elif d == 10:
    n_d = 5
  elif d == 5:
    n_d = 1
  else:
    return 1
  
  ways = 0
  for i in range(n/d+1):
    ways += make_change(n-i*d,n_d)
  return ways

def main():
  n = int(sys.argv[1])
  print make_change(n,25)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
