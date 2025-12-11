from array import array as arr

class Solution:
    def unionOfArray(self, arr1, arr2):
        i, j = 0, 0
        temp = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                if arr2[j] not in temp:
                    temp.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if arr2[j] not in temp:
                    temp.append(arr2[j])
                j += 1
            else:
                temp.append(arr1[i])
                j += 1
                i += 1
                
        while i < len(arr1):
            if arr1[i] not in temp:
                temp.append(arr1[i])
            i += 1
            
        while j < len(arr2):
            if arr2[j] not in temp:
                temp.append(arr2[j])
            j += 1
            
        return temp
    
sols = Solution()
arr1 = arr('i', {1,2,3,4,5,6,7,8,9,10})
arr2 = arr('i', {2,3,4,4,5,11,12})
print("Union of Arrays: ", sols.unionOfArray(arr1, arr2))