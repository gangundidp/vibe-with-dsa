from typing import *

class Solution:
    '''
    Given a 0-indexed n x m matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and 
    return the array [i, j]. A peak element in a 2D grid is an element that is strictly greater than all of its adjacent 
    neighbours to the left, right, top, and bottom. Assume that the entire matrix is surrounded by an outer
    perimeter with the value -1 in each cell.
    
    Example 1:
    Input:
    mat = [[5, 10, 8], [4, 25, 7], [3, 9, 6]]
    Output:
    [1, 1]
    Explanation:
    The value at index [1, 1] is 25, which is a peak because all its neighbors (10, 7, 4, 9) are smaller.

    Example 2:
    Input:
    mat = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
    Output:
    [2, 2]
    Explanation:
    The value at index [2, 2] is 9, which is a peak as it is greater than its neighbors (8, 4).
    '''
    # def findPeakElement(self, mat: List[List[int]], n: int, m: int) -> tuple:
    #     low, high = 0, m-1
        
    #     while (low <= high):
    #         mid = (low + high)//2
    #         max_ele, row = max(((mat[row][mid], row) for row in range(n)))
            
    #         if mat[row][mid - low - 1] < max_ele > mat[row][high - mid]:
    #             return (row, mid)

    #         if mat[row][mid - low -1] >= max_ele:
    #             high = mid + 1
    #         if mat[row][high - mid] >= max_ele:
    #             low = mid - 1
    #     return -1
    

    def maxElement(self, arr, col):
        n = len(arr)
        max_val = float('-inf')
        index = -1
  
        for i in range(n):
            if arr[i][col] > max_val:
                max_val = arr[i][col]
                index = i
  
        return index
  
      # Function to find a peak element in the 2D matrix 
      # using binary search 
    def findPeakGrid(self, arr):
        n = len(arr)    
        m = len(arr[0])  
  
        low = 0
        high = m - 1
  
        while low <= high:
            mid = (low + high) // 2

            row = self.maxElement(arr, mid)
  
              # Determine the elements to the left and right of 
              # the middle element in the found row
            left = arr[row][mid - 1] if mid - 1 >= 0 else float('-inf')
            right = arr[row][mid + 1] if mid + 1 < m else float('-inf')
  
              # Check if the middle element is greater than its neighbors
            if arr[row][mid] > left and arr[row][mid] > right:
                return [row, mid]
            elif left > arr[row][mid]:
                high = mid - 1
            else:
                low = mid + 1
  
          # Return [-1, -1] if no peak element is found
        return [-1, -1]
  
    
if __name__ == "__main__":
    sols = Solution()
    mat = [[5, 10, 8], [4, 25, 7], [3, 9, 6]]
    print("Ouput: ", sols.findPeakGrid(mat))
    mat = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
    print("Ouput: ", sols.findPeakGrid(mat))
    mat = [
      [4, 2, 5, 1, 4, 5],
      [2, 9, 3, 2, 3, 2],
      [1, 7, 6, 0, 1, 3],
      [3, 6, 2, 3, 7, 2]
  ]
    print("Output: ", sols.findPeakGrid(mat))