#!/usr/bin/python -tt

import sys
import time

def r_paren(n,m,paren_lst):
  if n == 0: 
    for i in range(m):
      paren_lst.append(')')
    print ''.join(paren_lst)
    for i in range(m):
      paren_lst.pop()
  else:
    paren_lst.append('(')
    r_paren(n-1,m,paren_lst)
    paren_lst.pop()   
    if m > n:
      paren_lst.append(')')
      r_paren(n,m-1,paren_lst)
      paren_lst.pop()

def main():
  n = int(sys.argv[1])
  r_paren(n,n,[])
      
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
