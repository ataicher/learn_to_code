# heap sort
import sys
from random import randint

class Heap(object):
  def __init__(self, A):
    self.length = len(A)
    self.heap_size = self.length
    self.data = A

  def left(self, i):
    return (i << 1) + 1

  def right(self, i):
    return (i << 1) + 2
    
  def parent(self, i): 
    return (i >> 1) - 1
      
def max_heapify(H,i):
  l = H.left(i)
  r = H.right(i)
  if l < H.heap_size and H.data[l] > H.data[i]:
    largest = l
  else:
    largest = i
  if r < H.heap_size and H.data[r] > H.data[largest]:
    largest = r
  if largest != i:
    tmp = H.data[i]
    H.data[i] = H.data[largest]
    H.data[largest] = tmp
    max_heapify(H, largest)

def build_max_heap(H):
  for i in xrange(H.length/2-1, -1, -1):
    max_heapify(H, i)
  
def heap_sort(A):
  H = Heap(A)
  build_max_heap(H)
  for i in xrange(H.length-1, 0, -1):
    tmp = H.data[i]
    H.data[i] = H.data[0]
    H.data[0] = tmp
    H.heap_size -= 1
    max_heapify(H, 0)
  return H.data

# main function that tests the code
def main():
  N = int(sys.argv[1])
  A = [0] * N
  for i in xrange(N):
    A[i] = randint(0,N)
  print A

  print heap_sort(A)

if __name__ == '__main__':
  main()
