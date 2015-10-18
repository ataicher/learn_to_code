#!/usr/bin/python -tt

import sys

def isAnagram(S1,S2):
  # remove white space
  S1 = S1.replace(' ',''); S2 = S2.replace(' ','')
  # check the string lengths are identical
  if len(S1) != len(S2):
    return False
  # set strings to lower case
  S1 = S1.lower(); S2 = S2.lower()
  # sort strings
  S1 = sorted(S1); S2 = sorted(S2)
  if S1 == S2:
    return True
  else:
    return False
    
def main():
  print 'find out if two strings are anagrams'
  if len(sys.argv) == 3:
    S1 = sys.argv[1]
    S2 = sys.argv[2]
    print 'S1 =', S1
    print 'S2 =', S2
  else:
    S1 = 'Namibia'
    S2 = 'I am a bin'
    print 'using default strings:\nS1 = Namibia\nS2 = I am a bin'
  
  
  if isAnagram(S1,S2):
    print 'the two strings are anagrams!'
  else:
    print 'sorry. The two strings are not anagrams'
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
