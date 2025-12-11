'''
Example:  
Input: nums = [1, 2, 3, 4, 5]  
Output: [2, 3, 4, 5, 1]  
Explanation: Initially, nums = [1, 2, 3, 4, 5]  
Rotating once to the left results in nums = [2, 3, 4, 5, 1].

'''
from array import array as arr

def rotateArrayByOne(arr):
    first_ele = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = first_ele
    
    return arr

if __name__ == "__main__":
    arr = arr('i', [3, 9, 0, 7, 4])
    print('Rotated by one left: ', rotateArrayByOne(arr))