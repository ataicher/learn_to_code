# heap sort
import sys
from random import randint

def partition(A,p,r):
  x = A[r-1]
  i = p-1
  for j in range(p,r-1):
    if A[j] <= x:
      i += 1
      tmp = A[i]
      A[i] = A[j]
      A[j] = tmp
  A[r-1] = A[i+1]
  A[i+1] = x
  return i+1

def quick_sort(A,p,r):
  if p < r:
    q = partition(A,p,r)
    quick_sort(A,p,q)
    quick_sort(A,q+1,r)

# main function that tests the code
def main():
  N = int(sys.argv[1])
  A = [0] * N
  for i in xrange(N):
    A[i] = randint(0,N)
  print A

  quick_sort(A,0,N)
  
  print A
  
if __name__ == '__main__':
  main()
