#!/usr/bin/python -tt
# determine if a string has all unique characters without using additional data structures

import sys

# determine if a string S has suplicate characters
def has_duplicates(S):
  for i in range(len(S)):
    for j in range(i+1,len(S)):
      if S[i] == S[j]:
        return True
  return False          

def has_duplicates2(S):
  ASCII_vals = [0]*256
  for i in range(len(S)):
    ch_int = ord(S[i])
    if ASCII_vals[ch_int]:
      return True
    else:
      ASCII_vals[ch_int] += 1
  return False

def main():
  
  # obtain user input or use default string
  print 'remove duplicate characters in a string'
  if len(sys.argv) >= 2:
    S = sys.argv[1]
    print 'S =', S
  else:
    S = 'abaccd'
    print 'using default string\nS = abaccd'

  # evaluate if string S has duplicate characters and print results
  if has_duplicates2(S):
    print 'string', S, 'has duplicate characters'
  else:
    print 'string',  S, 'has no duplicate characters'
                   
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
