#!/usr/bin/python -tt

import sys

def main():
  print 'remove duplicate characters in a string'
  if len(sys.argv) >= 2:
    S = sys.argv[1]
    print 'S =', S
  else:
    S = 'abaccd'
    print 'using default string\nS = abaccd'
    
  L = list(S)
  i = 0
  while i < len(L):
    popI = False
    j = i + 1
    while j < len(L):
      if L[i] == L[j]:
        L.pop(j)
        popI = True
      else:
        j = j + 1
    if popI:
      L.pop(i)
    else:
      i = i + 1
  S = ''.join(L)
  print 'S =', S

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
