from typing import * 

class Solution:
    def majorityElementBrute(self, arr: List[int]) -> List[int]:
        n = len(arr)
        lst = []
        for i in range(n):
            if ((len(lst)==0) or (lst[0] != arr[i])):
                cnt = 0
                for j in range(n):
                    if arr[j] == arr[i]:
                        cnt += 1
                if (cnt > (n//3)):
                    lst.append(arr[i])
            if (len(lst)==2):
                break
        return lst
    
    def majorityElementBetter(self, arr: List[int]) -> List[int]:
        n = len(arr)
        counter = Counter(arr)
        lst = []
        
        for num, count in counter.items():
            if count > (n//3):
                lst.append(num)
                
        return lst
    
sols = Solution()
arr = [1, 2, 1, 1, 3, 2]
print("Output: ", sols.majorityElementBrute(arr))
arr = [1, 2, 1, 1, 3, 2, 2]  
print("Output: ", sols.majorityElementBetter(arr))
                