#!/usr/bin/python -tt

import sys
import time

def r_fibonacci(n):
  if n > 2:
    return r_fibonacci(n-1) + r_fibonacci(n-2)
  else:
    return 1

def i_fibonacci(n):
  if n > 2:
    val_old = 1; val_new = 1
    for i in range(3,n+1):
      tmp = val_new
      val_new = val_old + val_new
      val_old = tmp
    return val_new
  else:
    return 1

def main():
  n = int(sys.argv[1])
  tic = time.clock()
  f_r = r_fibonacci(n)
  t_r = time.clock() - tic
  print t_r
  tic = time.clock()
  f_i = i_fibonacci(n)
  t_i = time.clock() - tic
  print t_i
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
