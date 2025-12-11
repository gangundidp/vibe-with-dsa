from array import array as arr

class Solution:
    # Time com: O(2n+k) Space com: O(k)
    def moveZeroes1(self, arr):
        temp = []
        
        for ele in arr:
            if ele == 0:
                temp.append(ele)

        i = 0
        for j in range(len(arr)):
            if arr[j] != 0:
                arr[i] = arr[j]
                i += 1
        
        for k in range(len(temp)):
            arr[i] = temp[k]
            i += 1
            
        return arr
    
    # Time com: O(2n) Space com: O(k)
    def moveZeroes2(self, arr):
        temp = []
        
        for ele in arr:
            if ele != 0:
                temp.append(ele)

        for i in range(len(temp)):
            arr[i] = temp[i]
            
        for j in range(len(temp), len(arr)):
            arr[j] = 0
            
        return arr
    
    # Time com: O(n) Space com: O(k)
    def moveZeroes3(self, arr):
        j = -1
        for i in range(len(arr)):
            if arr[i] == 0:
                j = i
                break
        if (j == -1):
            return arr # non-zeroes array
        
        for i in range(j+1, len(arr)):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        return arr
                
        
sol = Solution()
arr = arr('i',  [0, 1, 4, 0, 5, 2])
print('Solution: ', sol.moveZeroes1(arr))
print('Solution: ', sol.moveZeroes2(arr))
print('Solution: ', sol.moveZeroes3(arr))
