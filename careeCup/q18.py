#!/usr/bin/python -tt

import sys

def isSubstring(bigS,smallS):
  return bigS.find(smallS)+1

def main():
  print 'find out if a string is a rotation of another string'
  if len(sys.argv) >= 3:
    S1 = sys.argv[1]
    S2 = sys.argv[2]
    print S1
    print S2
  else:
    S1 = 'waterbottle'
    S2 = 'terbottlewa'
    print 'using default strings:'
    print S1
    print S2
  
  if len(S1) == len(S2):
    S1S1 = ''.join([S1, S1])
    isRotation = isSubstring(S1S1,S2)
  else:
    isRotation = False
  
  if isRotation:
    print 'the strings are rotations of each other'
  else:
    print 'the strings are not rotations of each other'
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
