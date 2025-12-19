from typing import *

class Solution:
    '''
    Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number 
    of rows and columns, respectively. The elements of each row and each column are sorted in non-decreasing order. 
    But, the first element of a row is not necessarily greater than the last element of the previous row (if it exists).
    You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.

    Examples
    Example 1:
    Matrix=
    1   4   7   11
    2   5   8   12
    3   6   9   16
    10 13  14  17
    Target: 9
    Output: Found at (2,2) (0-indexed)


    Example 2:
    Matrix=
    5   10  15
    6   12  18
    8   16  20
    Target: 7
    Output: Not Found
    '''
    
    def searchInTheRow(self, arr: List[int], target: int) -> int:
        low, high = 0, len(arr)-1
        
        while low <= high:
            mid = low + (high - low)//2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return False

    # Binary Search Method 1
    def searchUsingBSMethod1(self, mat: List[List[int]], n: int, m: int, target: int) -> int:
        for row in range(n):
            col = self.searchInTheRow(mat[row], target)
            if col:
                return f'Found at {(row,col)}'
        return 'Not found'
    
    
    def searchUsingBsMethod2(self, mat: List[List[int]], n: int, m: int, target: int) -> int:
        row, col = 0, m-1
        
        while (row < n and col >= 0):
            if mat[row][col] == target:
                return f'Found at {(row,col)}'
            if mat[row][col] < target:
                row += 1
            elif mat[row][col] > target:
                col -= 1
                
        return 'Not Found'
        
if __name__ == "__main__":
    sols = Solution()
    mat = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 10], [10, 13, 14, 17]]
    print('Output: ', sols.searchUsingBSMethod1(mat, 4, 4, 9))
    mat = [[5, 10, 15], [6, 12, 18], [8, 16, 24]]
    print('Output: ', sols.searchUsingBSMethod1(mat, 3, 3, 9))
    
    mat = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 10], [10, 13, 14, 17]]
    print('Output: ', sols.searchUsingBsMethod2(mat, 4, 4, 9))
    mat = [[5, 10, 15], [6, 12, 18], [8, 16, 24]]
    print('Output: ', sols.searchUsingBsMethod2(mat, 3, 3, 9))