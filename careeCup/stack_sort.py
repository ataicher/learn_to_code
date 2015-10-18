#!/usr/bin/python -tt

import sys
import time
from stacksheaps import Stack

def stack_sort(s):
  r = Stack()
  while not s.isEmpty():
    tmp = s.pop()
    while not r.isEmpty() and r.peek() > tmp:
      s.push(r.pop())
    r.push(tmp)
  return r

def main():
  s = Stack()
  s.push('3')
  s.push('5')
  s.push('2')
  s.push('6')
  s.push('4')
  s.push('1')
  print s
  raw_input('press any key to continue\n')
  r = stack_sort(s)
  print r
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
