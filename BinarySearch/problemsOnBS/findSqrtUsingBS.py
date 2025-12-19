from array import array as arr
from typing import *

class Solution:
    '''
    Problem Statement: You are given a positive integer n. 
    Your task is to find and return its square root. 
    If ‘n’ is not a perfect square, then return the floor value of sqrt(n).
    '''
    def findSquareRoot(self, input_num: int) -> int:
        ans = 0
        for i in range(1, input_num):
            if (i * i) <= input_num:
                ans = i
            else:
                return ans
        
    def findSquareRootBS(self, input_num: int) -> int:
        ans = 0
        low, high = 1, input_num
        
        while low <= high:
            mid = (low + high)//2

            if mid * mid <= input_num:
                low = mid + 1
                ans =  mid
            else:
                high = mid - 1
        return ans
    
if __name__ == "__main__":
    sols = Solution()
    num = int(input('Enter the input: '))
    print('Output: ', sols.findSquareRoot(num))
    print('Output: ', sols.findSquareRootBS(num))