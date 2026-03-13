import random

class Solution:
    def kthLargestElement(self, nums, k):
        # Return -1, if the Kth largest element does not exist
        if k > len(nums):
            return -1
        
        # Pointers to mark the part of working array 
        l, r = 0, len(nums) - 1
        
        # Until the Kth largest element is found
        while True:
            pivotIndex = self.randomIndex(l, r)
            
            pivotIndex = self.partitionAndReturnIndex(nums, pivotIndex, l, r)
            
            if pivotIndex == k - 1:
                return nums[pivotIndex]
            
            elif pivotIndex > k - 1:
                r = pivotIndex - 1
            else:
                l = pivotIndex + 1
                
    def randomIndex(self, l, r):
        length = r - l + 1
        
        return random.randint(l, r)

    def partitionAndReturnIndex(self, nums, pivotIndex, l, r):
        pivot = nums[pivotIndex]  # Get the pivot element
        
        nums[l], nums[pivotIndex] = nums[pivotIndex], nums[l]
        
        ind = l + 1
        
        for i in range(l + 1, r + 1):
            if nums[i] > pivot:
                nums[ind], nums[i] = nums[i], nums[ind]
                
                ind += 1
        
        nums[l], nums[ind - 1] = nums[ind - 1], nums[l]
        
        return ind - 1  # Return the index of pivot now

if __name__ == "__main__":
    sol = Solution()
    nums = [-5, 4, 1, 2, -3]
    k = 5


    ans = sol.kthLargestElement(nums, k)
    print("The Kth largest element in the array is:", ans)
