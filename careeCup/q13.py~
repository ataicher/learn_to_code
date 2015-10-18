#!/usr/bin/python -tt
# reverse a C-style string

import sys

def reverse_C_str(C_string):
  end = 0
  while C_string[end] != '\0':
    end += 1
  end -= 1
    
  i = 0
  while i < end:
    tmp = C_string[end]
    C_string[end] = C_string[i]
    C_string[i] = tmp
    end -= 1 
    i += 1
  return C_string

def main():
  
  # obtain user input or use default string, then add null character to end and convert to list
  print 'reverse a C-style string'
  if len(sys.argv) >= 2:
    S = sys.argv[1]
    if S[len(S)-1] != '\0':
      S = S + '\0'
    print 'S =', S
  else:
    S = 'abaccd\0'
    print 'using default string\nS = abaccd\0'
  C_string = []
  for char in S:
    C_string.append(char)
 
  # evalutae and print results
  C_string_rev = reverse_C_str(C_string)
  S_rev = ''.join(C_string_rev)
  print 'reversed string is', S_rev
                   
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
