#!/usr/bin/python -tt

import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import pylab
import time

def findMaxCrossingSubarray(A,low,mid,high):
  leftSum = float('-inf')
  sum = 0
  for i in range(mid-1,low-1,-1):
    sum = sum + A[i]
    if sum > leftSum:
      leftSum = sum
      maxLeft = i
  rightSum = float('-inf')
  sum = 0
  for j in range(mid,high):
    sum = sum + A[j]
    if sum > rightSum:
      rightSum = sum
      maxRight = j+1
  return(maxLeft,maxRight,leftSum+rightSum)

def findMaxSubarray(A,low,high):
  if high == low+1:
    return(low, high,A[low])
  else:
    mid = int(math.floor((low+high)/2))
    (leftLow,leftHigh,leftSum) = findMaxSubarray(A,low,mid)
    (rightLow,rightHigh,rightSum) = findMaxSubarray(A,mid,high)
    (crossLow,crossHigh,crossSum) = findMaxCrossingSubarray(A,low,mid,high)
    if leftSum >= rightSum and leftSum >= crossSum:
      return(leftLow,leftHigh,leftSum)      
    elif rightSum >= leftSum and rightSum >= crossSum:
      return(rightLow,rightHigh,rightSum)
    else:
      return(crossLow,crossHigh,crossSum)

def findMaxSubarrayBruteForce(A):
  maxSum = float('-inf')
  for i in range(len(A)):
    sum = 0
    for j in range(i,len(A)): 
      sum = sum + A[j]
      if sum > maxSum:
        maxSum = sum
        low = i
        high = j+1
  return(low,high,maxSum)

def findMaxSubarrayLinear(A):
  maxSum = A[0]
  low = 0
  high = 1
  lowJ = 0
  maxSumJ = A[0]
  for j in range(1,len(A)):
    if maxSumJ > 0:
      maxSumJ = maxSumJ + A[j]
    else:
      maxSumJ = A[j]
      lowJ = j
    if maxSumJ > maxSum:
      maxSum = maxSumJ
      low = lowJ
      high = j + 1
  return(low,high,maxSum)

def main():  
  if len(sys.argv) == 4:
    n = int(sys.argv[1])
    min = float(sys.argv[2])
    max = float(sys.argv[3])
    A = np.random.randint(min,max,n)
    print A
    #(low,high,sum) = findMaxSubarray(A,0,len(A))
    #(low,high,sum) = findMaxSubarrayBrute(A)
    (low,high,sum) = findMaxSubarrayLinear(A)
   
    print 'max subarray sum is %d for A[%d:%d]' % (sum,low,high)
    
  elif len(sys.argv) == 6:
    nMin = int(sys.argv[1])
    nMax = int(sys.argv[2])
    nIter = int(sys.argv[3])
    min = float(sys.argv[4])
    max = float(sys.argv[5])
    timeCrossing = []
    timeBrute = []
    timeLinear = []
    #print range(nMin,nMax,(nMax-nMin)/nIter)
    for i in range(math.floor(log(n))):
      nSteps.append(2^i)
    for n in range(nMin,nMax,(nMax-nMin)/nIter):
      A = np.random.randint(min,max,n)
      tic = time.clock()
      (low,high,sum) = findMaxSubarray(A,0,len(A))
      timeCrossing.append(time.clock()-tic)
      tic = time.clock()
      (low,high,sum) = findMaxSubarrayBruteForce(A)    
      timeBrute.append(time.clock()-tic)
      tic = time.clock()
      (low,high,sum) = findMaxSubarrayLinear(A)    
      timeLinear.append(time.clock()-tic)
    
    n = np.array(range(nMin,nMax,(nMax-nMin)/nIter))
    n2 = np.square(n)*timeBrute[0]
    nlogn = np.log2(n)*n*timeCrossing[0]

    '''plt.subplot(2,2,1)
    plt.plot(n,timeCrossing,'b')
    plt.plot(n,nlogn,'g')
    plt.subplot(2,2,2)
    plt.plot(n,timeBrute,'b')
    plt.plot(n,n2,'g')
    plt.subplot(2,2,3)
    plt.plot(n,timeLinear,'b')
    plt.plot(n,n*timeLinear[0],'g')
    plt.title('max subarray sum algorithms')
    plt.xlabel('number of elements')
    plt.ylabel('time (?ms)')
    plt.subplot(2,2,4)'''
    plt.figure(1)
    plt.loglog(n,timeCrossing,'b',label  = 'crossing')
    plt.loglog(n,nlogn,'g',label = 'nlog(n)')
    plt.loglog(n,timeBrute,'r',label = 'brute force')
    plt.loglog(n,n2,'c', label = 'n^2')
    plt.loglog(n,timeLinear,'m', label = 'linear')
    plt.loglog(n,n*timeLinear[0],'y', label = 'n')
    plt.xlabel('number of elements n')
    plt.ylabel('time(s)')

    plt.legend()
    
    pylab.show()

  elif len(sys.argv) == 1:
    print 'default array:'
    print 'A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]'
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print 'max subarray sum:'
    print '  true solution: 43 for A[7:11]'
    (low,high,sum) = findMaxSubarray(A,0,len(A))
    print '  recursive crossing algorithm: %d for A[%d:%d]' % (sum,low,high)
    (low,high,sum) = findMaxSubarrayBruteForce(A)
    print '  brute force algorithm: %d for A[%d:%d]' % (sum,low,high)
    (low,high,sum) = findMaxSubarrayLinear(A)
    print '  linear algorithm: %d for A[%d:%d]' % (sum,low,high)
  
    print '\ntesting with all negative array:'
    print 'A = [-6 , -4 , -3, -20, -2, -9]'
    A = [-6,-4,-3,-20,-2,-9]
    print 'max subarray sum:'
    print '  true solution: -2 for A[4:5]'
    (low,high,sum) = findMaxSubarray(A,0,len(A))
    print '  recursive crossing algorithm: %d for A[%d:%d]' % (sum,low,high)
    (low,high,sum) = findMaxSubarrayBruteForce(A)
    print '  brute force algorithm: %d for A[%d:%d]' % (sum,low,high)
    (low,high,sum) = findMaxSubarrayLinear(A)
    print '  linear algorithm: %d for A[%d:%d]' % (sum,low,high)

    print '\ntesting with array containing zeros:'
    print 'A = [6 , 4 , -3, 20, 0, -9]'
    A = [6,4,-3,20,0,-9]
    print 'max subarray sum:'
    print '  true solution: 27 for A[0:4] or A[0:5]'
    (low,high,sum) = findMaxSubarray(A,0,len(A))
    print '  recursive crossing algorithm: %d for A[%d:%d]' % (sum,low,high)
    (low,high,sum) = findMaxSubarrayBruteForce(A)
    print '  brute force algorithm: %d for A[%d:%d]' % (sum,low,high)
    (low,high,sum) = findMaxSubarrayLinear(A)
    print '  linear algorithm: %d for A[%d:%d]' % (sum,low,high)

    print '\ntesting with array with two max subarrays:'
    print 'A = [6 , 4 , -12, 10, -2, -9, 2]'
    A = [6,4,-12,10,-2,-9,2]
    print 'max subarray sum:'
    print '  true solution: 10 for A[0:2] or A[3:4]'
    (low,high,sum) = findMaxSubarray(A,0,len(A))
    print '  recursive crossing algorithm: %d for A[%d:%d]' % (sum,low,high)
    (low,high,sum) = findMaxSubarrayBruteForce(A)
    print '  brute force algorithm: %d for A[%d:%d]' % (sum,low,high)
    (low,high,sum) = findMaxSubarrayLinear(A)
    print '  linear algorithm: %d for A[%d:%d]' % (sum,low,high)

  else:
    print 'error: incopatible number of inputs'
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
