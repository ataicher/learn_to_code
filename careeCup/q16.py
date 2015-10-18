#!/usr/bin/python -tt

import sys

def rotate_matrix(M,n):
  for i in range(n/2):
    for j in range(i,n-1-i):
      tmp = M[i][i+j]
      M[i][i+j] = M[-1-i-j][i]
      M[-1-i-j][i] = M[-1-i][-1-i-j]
      M[-1-i][-1-i-j] = M[i+j][-1-i]
      M[i+j][-1-i] = tmp
  
def print_matrix(M,n):
  for i in range(n):
    print M[i]
  print '\n'
  
def main():
  print 'rotate a NxN pixel image 90 degrees.  Image is represted by an NxN list of numbers 1 to N^2'
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
  else:
    n = 4
    print 'using default 4x4 matrix:'
 
  M = [[n*i+j for j in range(n)] for i in range(n)] 
  print_matrix(M,n)
  rotate_matrix(M,n)
  print_matrix(M,n)
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
