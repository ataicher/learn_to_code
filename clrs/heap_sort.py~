# insertion sort algorithm for sorting a list of numbers in
# non-decreasing order
def insertion_sort(A):
  for j in range(1,len(A)):
    key = A[j]
    i = j
    while i > 0 and A[i-1] > key:
      A[i] = A[i-1]
      i = i - 1
    A[i] = key
  return A

# insertion sort algorithm for sorting a list of numbers in
# non-increasing order
def reverse_insertion_sort(A):
  for j in range(1,len(A)):
    key = A[j]
    i = j
    while i > 0 and A[i-1] < key:
      A[i] = A[i-1]
      i = i - 1
    A[i] = key
  return A


# linear search algorithm for finding a particular value in a list
def linear_search(A,v):
  i = 0
  while A[i] != v:
    i = i + 1
    if i == len(A):
      return None
  return i

# adding two n-bit integers, stored in two n-element lists A, B. The sum should be stored in a (n+1)-bindary list C
import math
def binary_add(A,B,n):
  rem = 0
  C = []
  for i in range(n):
    C.append(int(math.fmod(A[i]+B[i]+rem,2)))
    rem = (A[i] + B[i] + rem)/2
  if rem == 1:
    C.append(1)
  return C

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

# main function that tests the code
def main():
  print
  print 'insertion_sort'
  test(insertion_sort([1 , 3 , 2]), [1 , 2 , 3])
  test(insertion_sort([4 , 2 , 2 , 1]),[1 , 2 , 2 , 4])
  test(insertion_sort([1.2 , 1 , 4, -2 , 'a']),[ -2 , 1 , 1.2 , 4 , 'a'])

  print
  print 'reverse_insertion_sort'
  test(reverse_insertion_sort([1 , 3 , 2]), [3 , 2 , 1])
  test(reverse_insertion_sort([4 , 2 , 2 , 1]),[4 , 2 , 2 , 1])
  test(reverse_insertion_sort([1.2 , 1 , 4, -2 , 'a']),[ 'a' , 4 , 1.2 , 1 , -2])

  print
  print 'linear_search'
  test(linear_search([1 , 3 , 5 , 2] , 2), 3)
  test(linear_search([1 , 4 , 3], 2), None)
  test(linear_search([.5, 1 , 1 , 3] , 1), 1)

  print
  print 'binary_add'
  test(binary_add([1, 0 , 1 , 1], [1 , 0 , 0 , 1], 4),[0 , 1 , 1, 0 , 1])
  test(binary_add([1 , 0 , 1], [1 , 1 , 1], 3),[0 , 0 , 1 , 1])

if __name__ == '__main__':
  main()
