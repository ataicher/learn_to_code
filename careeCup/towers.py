#!/usr/bin/python -tt

import sys
import time
from stacks_queues import Stack

def create_sorted_stack(n):
  s = Stack()
  for i in range(1,n+1):
    s.push(str(i))
  return s

def stackPrint(stacks):
  print 'stack0: ', stacks[0]
  print 'stack1: ', stacks[1]
  print 'stack2: ', stacks[2], '\n'

def move(stacks,i,j,m,totMoves):
  if m > 1:
    nij = 3 - (i + j)
    totMoves = move(stacks,i,nij,m-1, totMoves)
    stacks[j].push(stacks[i].pop());  totMoves += 1; #stackPrint(stacks); time.sleep(.4)
    totMoves = move(stacks,nij,j,m-1, totMoves)
  else:
    stacks[j].push(stacks[i].pop());  totMoves += 1; #stackPrint(stacks); time.sleep(.4) 
  return totMoves
def main():
  
  totMoves_lst = []
  for n in range(1,10):  
    stacks = [create_sorted_stack(n), Stack(), Stack()]
    #stackPrint(stacks)
    #raw_input('press any key to continue\n')
    totMoves_lst.append(move(stacks,0,2,n,0))  
  print 'total number of moves:', totMoves_lst, '\n'
  #stackPrint(stacks)
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
