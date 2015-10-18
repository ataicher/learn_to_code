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
  def __init__(self,A = []):
    if isinstance(A, int)
      self.root = Node(A)
    elif: isinstance(A, list)
      if A:
        self.root = Node(A[0])
        for key in A[1:]:
          T.insert(A,key)
      else:
        self.root = Node()
    else:
      return 'invalid input to create BST'

  def insert(self,z):
    y = None
    x = self.root
    while x:
      y = x
      if z.val < x.val:
        x = x.left
      else:
        x = x.right
    if z.key < y.key:
      y.left = z
    else:
      y.right = z

  def __str__(self):
   def inorder_iterate(self):
     if self.root is None:
       print 'empty BST'
     stk=[]
     stk.append((self.root,'not done'))
     while len(stk)>0:
       u,state=stk.pop()
       if state=='not done':
         if u.right is not None:
           stk.append((u.right,'not done'))
         stk.append((u,'done'))
         if u.left is not None:
           stk.append((u.left,'not done'))
       else: #state=='done'
         print A
    
def create_BST(A):

  BST = 

# main function that tests the code
def main():
  N = int(sys.argv[1])
  A = [0] * N
  for i in xrange(N):
    A[i] = randint(0,N)

  create_BST(A)

  print A

  quick_sort(A,0,N)
  
  print A
  
if __name__ == '__main__':
  main()
