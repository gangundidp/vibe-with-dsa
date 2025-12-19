from typing import *

class Solution:
    '''
    Problem Statement:
    Given a row-wise sorted matrix of size M*N, where M is no. of rows and N is no. of columns, find the median in the given matrix.
    Note: M*N is odd.

    Examples
    Input: M = 3, N = 3, matrix[][] =

    1 4 9 
    2 5 6
    3 8 7
    Output: 5
    Explanation: 
    If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. Therefore, median = 5

    Input: M = 3, N = 3, matrix[][] =

    1 3 8 
    2 3 4
    1 2 5
    Output: 3
    Explanation: 
    If we find the linear sorted array, the array becomes 1 1 2 2 3 3 4 5 7 8. Therefore, median = 3.
    '''
    
    def findMedian(self, mat: List[List[int]], n: int, m: int) -> int:
        sorted_array = [mat[row][col] for row in range(n) for col in range(m)]
        sorted_array.sort()

        median = len(sorted_array)//2
        
        return sorted_array[median]
    
    
    def upperBound(self, nums: List[int], target: int) -> int:
        ans = len(nums)
        low, high = 0, len(nums)-1
        
        while (low <= high):
            mid = (low + high)//2

            if nums[mid] <= target:
                low = mid + 1
            else:
                ans = mid # upper bound means greater, here mid element is greater than target (nums[mid]>target)
                high = mid - 1
        return ans
    
    def countSmallerEquals(self, mat: List[List[int]], mid: int) -> int:
        count = 0
        for row in range(len(mat)):
            count += self.upperBound(mat[row], mid)
        # print(mid, count)
        return count
    
    def findMedianBS(self, mat: List[List[int]], n: int, m: int) -> int:
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        req = (n * m + 1)//2
        
        while (low < high):
            mid = (low + high)//2
            
            smallerEquals = self.countSmallerEquals(mat, mid)

            if (smallerEquals < req):
                low = mid + 1
            else:
                high = mid
        return low
    
if __name__ == "__main__":
    sols = Solution()
    mat = [[1, 4, 9], [2, 5, 6], [3, 7, 8]]
    print("Output: ", sols.findMedian(mat, 3, 3))
    mat = [[1, 3, 8], [2, 3, 4], [1, 2, 5]]
    print("Output: ", sols.findMedian(mat, 3, 3))
    
    mat = [[1, 4, 9], [2, 5, 6], [3, 7, 8]]
    print("Output: ", sols.findMedianBS(mat, 3, 3))
    mat = [[1, 3, 8], [2, 3, 4], [1, 2, 5]]
    print("Output: ", sols.findMedianBS(mat, 3, 3))
    mat = [[1, 5, 7, 9, 11], [2, 3, 4, 5, 10], [9, 10, 12, 14, 16]]
    print("Output: ", sols.findMedianBS(mat, 3, 5))