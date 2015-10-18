#!/usr/bin/python -tt

import sys

def replace_spaces(S_list):
  # find new length of the string
  length = 0
  while S_list[length] != '\0':
    length += 1
  new_length = length
  for char in S_list:
    if char == ' ':
      new_length += 2
  
  # replace spaces with the chars '%20'
  for i in range(length-1,0,-1): 
    if S_list[i] == ' ':
      S_list[new_length - 1] = '0'
      S_list[new_length - 2] = '2'
      S_list[new_length - 3] = '%'
      new_length -= 3
    else:
      S_list[new_length - 1] = S_list[i]
      new_length -= 1
  
def main():
  print 'replace the spaces in a string with the chars \'%20\''
  if len(sys.argv) == 2:
    S = sys.argv[1]
    print 'S =', S
  else:
    S = 'hello world '
    print 'using default string:\nS = hello world '
  
  # ensure string is long enough
  S = S + '\0'*100
  # convert string into mutable list of chars
  S_list = []
  for char in S:
    S_list.append(char)
  
  replace_spaces(S_list)
  S = ''.join(S_list)
  print 'new string = ' + S
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
