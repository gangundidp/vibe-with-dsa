import random

class Solution:
    def kthLargestElement(self, nums, k):
        # Return -1, if the Kth largest element does not exist
        if k > len(nums):
            return -1
        
        l, r = 0, len(nums) - 1
        
        while True:
            pivot_idx = self.randomIndex(l, r)
            
            pivot_idx = self.partitionAndReturnIndex(nums, pivot_idx, l, r)
            
            if pivot_idx == k - 1:
                return nums[pivot_idx]
            
            elif pivot_idx > k - 1:
                r = pivot_idx - 1
            else:
                l = pivot_idx + 1
                
    def randomIndex(self, l, r):
        length = r - l + 1
        
        return random.randint(l, r)

    def partitionAndReturnIndex(self, nums, pivot_idx, l, r):
        pivot = nums[pivot_idx]  # Get the pivot element
        
        nums[l], nums[pivot_idx] = nums[pivot_idx], nums[l]
        
        ind = l + 1  # Index to mark the start of r portion
        
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
