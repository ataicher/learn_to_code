#!/usr/bin/python -tt

import sys
from random import randint
from random import shuffle

# find the missing integer in a list
def missing_number(lst, nums):
    sorted_lst = sorted(lst)
    for i in range(nums):
        if i != sorted_lst[i]:
            return i
    return nums
      
def main():
    # get number of integers and generate a random permutation from [0,...,nums] 
    # with a random number missing
    nums = int(sys.argv[1])
    lst = range(nums+1)
    true_missing_number = randint(0,nums) 
    lst.remove(true_missing_number)
    shuffle(lst)
    print "find the missing number in the list:", lst    
    
    # find the missing number
    calc_missing_number = missing_number(lst, nums)
   
    # check for correctness
    if true_missing_number == calc_missing_number:
        print "found the missing number:", calc_missing_number
    else:
        print "failed to find correct missing number.", calc_missing_number, "!=", true_missing_number

    n = int(sys.arg[1])
    
        
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
