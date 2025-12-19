from typing import *

class Solution:
    '''
    Docstring for Solution
    Problem Statement: You have been given a non-empty grid ‘mat’ with 'n' rows and 'm' columns consisting of only 0s and 1s. All the rows are sorted in ascending order. Your task is to find the index of the row with the maximum number of ones. Note: If two rows have the same number of ones, consider the one with a smaller index. If there's no row with at least 1 zero, return -1

    Examples
    Example 1:
    Input Format: n = 3, m = 3, 
    mat[] = 
    1 1 1
    0 0 1
    0 0 0
    Result: 0
    Explanation: The row with the maximum number of ones is 0 (0 - indexed).

    Example 2:
    Input Format: n = 2, m = 2 , 
    mat[] = 
    0 0
    0 0
    Result: -1
    Explanation:  The matrix does not contain any 1. So, -1 is the answer.
    '''
    def findRowWithMaxNOof1s(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        maxCnt = 0
        ans = -1
        for row in range(n):
            cnt = 0
            for col in range(m):
                if mat[row][col] == 1:
                    cnt += 1
            
            if cnt > maxCnt:
                maxCnt = cnt
                ans = row
            
        return ans
    
    def findLowerBoundOfOne(self, target: int, low: int, high: int, arr: List[int]) -> int:
        mid = (low + high)//2
        if (low > high):
            if (low == len(arr)):
                return len(arr)
            else:
                if (arr[low] > target):
                    return low
                else:
                    return low+1

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return self.findLowerBoundOfOne(target, low, mid-1, arr)
        elif target > arr[mid]:
            return self.findLowerBoundOfOne(target, mid+1, high, arr)
        
    def findRowWithMaxOnesUsingBS(self, mat: List[List[int]], n: int, m: int) -> int:
        maxCnt = 0
        ans = -1
        
        for row in range(n):
            no_of_ones = m - self.findLowerBoundOfOne(1, 0, m-1, mat[row])

            if no_of_ones > maxCnt:
                maxCnt = no_of_ones
                ans = row
        return ans
            
    

if __name__ == "__main__":
    sols = Solution()
    mat = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    print("Output: ", sols.findRowWithMaxNOof1s(mat))
    print("Output: ", sols.findRowWithMaxOnesUsingBS(mat, 3, 3))
    mat = [[0, 0], [0, 0]]
    print("Output: ", sols.findRowWithMaxNOof1s(mat))
    print("Output: ", sols.findRowWithMaxOnesUsingBS(mat, 2, 2))
