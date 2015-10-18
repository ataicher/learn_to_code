#!/usr/bin/python -tt

import sys

def is_smaller(S):
  if len(S) == 0:
    return 0
  current_char = S[0]
  space_reduced = -1
  for char in S[1:]:
    if char == current_char:
      space_reduced += 1
    else:
      current_char = char
      space_reduced -= 1
  return space_reduced
    
def compress(S):
  S_comp_lst = []
  current_char = S[0]
  duplicates = 1
  for char in S[1:]:
    if char == current_char:
      duplicates += 1
    else:   
      S_comp_lst.append(current_char)
      S_comp_lst.append(str(duplicates))
      current_char = char
      duplicates = 1
  S_comp_lst.append(current_char)
  S_comp_lst.append(str(duplicates)) 
  return  ''.join(S_comp_lst)

def main():
  print 'compress a string with duplicate adjacent characters'
  if len(sys.argv) == 2:
    S = sys.argv[1]
    print 'S =', S
  else:
    S = 'aabcccccaaa'
    print 'using default string:\nS = aabcccccaaa '
  
  # ensure that the string is compressed
  space_reduced = is_smaller(S)
  if space_reduced > 0:
    S_comp = compress(S)
    print 'new string =', S_comp, 'requires', space_reduced , 'less chars to store'
  else:
    print 'the compression algorithm could not reduce the size of the string S = ' + S
  
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
