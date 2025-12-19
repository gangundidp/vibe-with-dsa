from array import array as arr
from typing import *

class Solution:
    def findNthRoot(self, input_num: int, root_num: int) -> int:
        for i in range(1, input_num):
            if (i ** root_num) == input_num:
                return i
        return -1
    
    def findNthRootBS(self, input_num: int, root_num: int) -> int:
        low, high = 1, input_num
        
        while low <= high:
            mid = (low + high)//2

            if mid ** root_num == input_num:
                return mid
            elif mid**root_num < input_num:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
if __name__ == '__main__':
    sols = Solution()
    num = int(input('Input: '))
    root_num=int(input('root_num: '))
    print('Output: ', sols.findNthRoot(num, root_num))
    print('Output: ', sols.findNthRootBS(num, root_num))