#!/usr/bin/python -tt

import sys
import math

def merge(A,p,q,r):
  
  n1 = (q+1)-p
  n2 = r-q
  
  L = []
  for i in range(n1):
      L.append(A[p+i])
  #L.append(float('inf'))
  R = []
  for j in range(n2):
      R.append(A[q+1+j])
  #R.append(float('inf'))

  i = 0; j = 0
  for k in range(p,r+1):
      
      if L[i] <= R[j]:
          A[k] = L[i]
          i += 1
          if i == n1:
              for l in range(j,n2):
                  A[k+l-j+1] = R[l]
              break
      
      else:
          A[k] = R[j]
          j += 1
          if j == n2:
              for l in range(i,n1):
                  A[k+l-i+1] = L[l]
              break
         
def merge_sort(A,p,r):
    if p < r:
        q = int(math.floor((p+r)/2))
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

def main():  
  
    if len(sys.argv) > 1:
        A = sys.argv[1]
    else:
        A = [1, 3, 6, 8, 2, 4, 7, 5]
        print 'using default list:\nA = [ 1, 3, 6, 8, 2, 4, 7, 5]\n'
    n = len(A)
  
    merge_sort(A,0,n-1)
  
    print A

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
