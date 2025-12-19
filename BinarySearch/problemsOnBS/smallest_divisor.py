from array import array as arr
from typing import *
from math import ceil

class Solution:
    '''
    Problem Statement: You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'. 
    Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given 
    array by it, the sum of the division's result is less than or equal to the given threshold value.

    Examples
    Example 1:
    Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
    Result: 3
    Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
    The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

    Example 2:
    Input Format: N = 4, arr[] = {8,4,2,3}, limit = 10
    Result: 2
    Explanation: If we choose 1, we get 17 as the sum. If we choose 2, we get 9(4+2+1+2) <= 10 as the answer. So, 2 is the answer.

    '''
    
    def findSmallestDivisor(self, nums: List[int], threshold: int)-> int:
        max_val = max(nums)

        for i in range(1, max_val + 1):
            sum = 0
            for num in nums:
                sum += ceil(num/i)
            
            if sum <= threshold:
                return i
        
        
    def findSum(self, nums: List[int], mid: int) -> int:
        sum = 0
        for num in nums:
            sum += ceil(num/mid)
            
        return sum
        
    def findSmallestDivisorUsingBS(self, nums: List[int], threshold: int) -> int:
        low, high = min(nums), max(nums)
        ans = 0
        while (low <= high):
            mid = (low + high)//2
            
            sum = self.findSum(nums, mid)
            if (sum <= threshold):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
            
            
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [1, 2, 3, 4, 5])
    print('Output: ', sols.findSmallestDivisor(nums, 8))
    nums = arr('i', [8, 4, 2, 3])
    print('Output: ', sols.findSmallestDivisor(nums, 10))
    
    nums = arr('i', [1, 2, 3, 4, 5])
    print('Output: ', sols.findSmallestDivisorUsingBS(nums, 8))
    nums = arr('i', [8, 4, 2, 3])
    print('Output: ', sols.findSmallestDivisorUsingBS(nums, 10))
    nums = arr('i', [1, 2, 5, 9])
    print('Output: ', sols.findSmallestDivisorUsingBS(nums, 6))
    