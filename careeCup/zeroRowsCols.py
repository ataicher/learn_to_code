#!/usr/bin/python -tt

import sys
import numpy as np

def main():
  print 'set to zero rows and columns that have a zero entry in an mxn matrix'
  if len(sys.argv) >= 2:
    M = np.matrix(sys.argv[1])
    print M
  else:
    M = np.matrix('1 2 3 0 ; 1 2 3 4 ; 0 2 3 4; 1 2 3 4')
    print 'using default matrix:'
    print M

  (m,n) = M.shape
  rows = range(m); cols = range(n)
  nonZeroCols = cols
  zeroRows = []; zeroCols = []
  for i in rows:
    j = nonZeroCols[0]
    while j < len(nonZeroCols):
      if M[i,j] == 0:
        zeroRows.append(i); zeroCols.append(j)
        break
      j = j + 1

  for j in zeroCols:
    for i in rows:
      M[i,j] = 0
  for i in zeroRows:
    for j in nonZeroCols:
      M[i,j] = 0
  
  print 'the new matrix:'
  print M
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
