from array import array as arr
from typing import *

class Solution:
    '''
    Problem Statement: You are given a strictly increasing array ‘vec’ and a positive integer 'k'. Find the 'kth' positive integer missing from 'vec'.

    Examples
    Example 1:
    Input Format: vec[]={4,7,9,10}, k = 1
    Result: 1
    Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.

    Example 2:
    Input Format: vec[]={4,7,9,10}, k = 4
    Result: 5
    Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 4, the fourth missing element is 5.

    '''
    
    def findKthMissingNumber(self, nums: List[int], k: int) -> int:
        '''
        Algorithm
        We will use a loop to traverse the array.
        Inside the loop,
        If vec[i] <= k: we will simply increase the value of k by 1.
        Otherwise, we will break out of the loop.
        Finally, we will return the value of k.
        '''
        
        # count = 0
        # for i in range(1, max(nums)):
        #     if i not in nums:
        #         count += 1
        #     if count == k:
        #         return i
        
        for i in nums:
            if i <= k:
                k += 1
            else:
                break
        return k
    
    def findKthMissingNumberUsingBS(self, nums: List[int], k: int) -> int:
        '''
        We cannot apply binary search on the answer space here as we cannot assure which missing number has the possibility of being the kth missing number. That is why, we will do something different here. We will try to find the closest neighbors (i.e. Present in the array) for the kth missing number by counting the number of missing numbers for each element in the given array.

        Algorithm
        Start by setting two markers: one at the beginning and one at the end of the list.
        Keep checking the middle position between the two markers by taking their average.
        Count how many numbers are missing up to that middle position by subtracting the expected number from the actual number found at that point.
            If the number of missing values is less than the desired position, move your focus to the right side of the list by shifting the beginning marker ahead.
            If not, move your focus to the left side by shifting the end marker backward.
        Once you've narrowed down the search and exited the loop, return the final answer by adding the desired position to the last marker you checked (plus one).

        '''
        
        low, high = 0, len(nums)-1
        
        while (low <= high):
            mid = low + (high - low) // 2
            
            missing = nums[mid] - (mid + 1) # number at that index - actual number
            
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
                
        return k + high + 1
            
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [4, 7, 9, 10])
    print('Output: ', sols.findKthMissingNumber(nums, 1))
    print('Output: ', sols.findKthMissingNumber(nums, 4))
    print('Output: ', sols.findKthMissingNumber(nums, 6))
    
    print('Output: ', sols.findKthMissingNumberUsingBS(nums, 1))
    print('Output: ', sols.findKthMissingNumberUsingBS(nums, 4))
    print('Output: ', sols.findKthMissingNumberUsingBS(nums, 6))