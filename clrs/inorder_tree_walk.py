# heap sort
import sys
from random import randint

class Node(object):
  def __init__(self,key=None):
    self.key = key
    self.right = None
    self.left = None
  def __str__(self):
    print 'node:'

class BST(object):
  def __init__(self, A = []):
    if A:
      self.root = Node(A[0])
      for key in A[1:]:
        self.insert(key)
    else:
        self.root = Node()
    
  def insert(self,key):
    y = None
    x = self.root
    while x:
      y = x
      if key < x.key:
        x = x.left
      else:
        x = x.right
    if key < y.key:
      y.left = Node(key)
    else:
      y.right = Node(key)

  def __str__(self):
    if not self.root:
       return 'empty BST'
    stk = []
    lst = []
    curr = self.root
    while curr:
      stk.append(curr)
      curr = curr.left
      while not curr and stk:
        node = stk.pop()
        lst.append(node.key)
        curr = node.right
    return str(lst)

# main function that tests the code
def main():
  N = int(sys.argv[1])
  A = [0] * N
  for i in xrange(N):
    A[i] = randint(0,N)
  print A
  t = BST(A)
  print t
  
if __name__ == '__main__':
  main()
