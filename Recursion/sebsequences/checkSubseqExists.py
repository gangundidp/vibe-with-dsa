from typing import *

def checkSubseqExists(nums: List, idx: int, sum: int) -> int:
    if sum == 0:
        return 1
    
    if sum < 0 or idx >= len(nums):
        return 0
    
    return checkSubseqExists(nums, idx+1, sum - nums[idx]) + checkSubseqExists(nums, idx+1, sum) 

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 8
    print("Output: ", end="")
    if checkSubseqExists(nums, 0, k):
        print("True")
    else:
        print("False")