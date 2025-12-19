from typing import *

class Solution:
    '''
    Problem Statement: You have been given a 2-D array 'mat' of size 'N x M' where 'N' and 'M' denote the number 
    of rows and columns, respectively. The elements of each row are sorted in non-decreasing order.
    Moreover, the first element of a row is greater than the last element of the previous row (if it exists).
    You are given an integer ‘target’, and your task is to find if it exists in the given 'mat' or not.

    Examples
    Input :mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], target = 8
    Output :True.
    Explanation :The target = 8 exists in the 'mat' at index (1, 3).

    Input :mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ], target = 78
    Output :false.
    Explanation :The target = 78 does not exist in the 'mat'. Therefore in the output, we see 'false'.
    '''
    
    # Linear Search
    def SearchIn2DArray(self, mat: List[List[int]], n: int, m: int, target: int) -> int:
        for row in range(n):
            for col in range(m):
                if mat[row][col] == target:
                    return True
        return False
    
    
    def searchInTheRow(self, arr: List[int], target: int) -> int:
        low, high = 0, len(arr)-1
        
        while low <= high:
            mid = low + (high - low)//2
            
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return False

    # Binary Search Method 1
    def searchIn2DArrayUsingBs(self, mat: List[List[int]], n: int, m: int, target: int) -> int:
        for row in range(n):
            if self.searchInTheRow(mat[row], target):
                return True
        return False
    
    # Binary Search Method 2
    def searchIn2DArrayUsingBsMethod2(self, mat: List[List[int]], n: int, m: int, target: int) -> bool:
        low, high = 0, len(mat)-1
        
        while low <= high:
            mid = (low + high)//2
            
            if mat[mid][0] <= target <= mat[mid][m-1]:
                return self.searchInTheRow(mat[mid], target)
            
            if mat[mid][m-1] > target:
                high = mid -1
            else:
                low = mid + 1
        return False


if __name__ == "__main__":
    sols = Solution()
    mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
    print('Output: ', sols.SearchIn2DArray(mat, 4, 4, 8))
    mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
    print('Output: ', sols.SearchIn2DArray(mat, 3, 3, 72))
    
    mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
    print('Output: ', sols.searchIn2DArrayUsingBs(mat, 4, 4, 8))
    mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
    print('Output: ', sols.searchIn2DArrayUsingBs(mat, 3, 3, 72))
    
    mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
    print('Output: ', sols.searchIn2DArrayUsingBsMethod2(mat, 4, 4, 8))
    mat = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
    print('Output: ', sols.searchIn2DArrayUsingBsMethod2(mat, 3, 3, 72))