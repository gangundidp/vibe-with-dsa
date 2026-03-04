class Solution:
    def longestOnesBrute(self, nums, k):
        n = len(nums)
        max_len = 0
        for i in range(n):
            
            zeros_count = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeros_count += 1
                    
                if zeros_count > k:
                    break
                
                curr_len = j - i + 1
                max_len = max(max_len, curr_len)
                
        return max_len
    
    def maxConsecutiveOnes(self, nums, k):
        n = len(nums)
        l, r, max_len = 0, 0, 0
        
        zeroes_count = 0
        while r < n:
            if nums[r] == 0:
                zeroes_count += 1
            
            # Shrink window from the left until the zeros_count back within limit 
            while zeroes_count > k:
                if nums[l] == 0:
                    zeroes_count -= 1
                l += 1
                
            curr_len = r - l + 1
            max_len = max(max_len, curr_len)
            r += 1
            
        return max_len
        
    def maxConsecutiveOnesOptimal(self, nums, k):
        n = len(nums)
        l, r, max_len = 0, 0, 0
        
        zeroes_count = 0
        while r < n:
            if nums[r] == 0:
                zeroes_count += 1
            
            if zeroes_count > k:
                if nums[l] == 0:
                    zeroes_count -= 1    
                l += 1
                # continue
                
            curr_len = r - l + 1
            
            max_len = max(max_len, curr_len)
            r += 1
        return max_len

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 3

    print("Output: ", sol.longestOnesBrute(nums, k))
    print("Output: ", sol.maxConsecutiveOnes(nums, k))
    print("Output: ", sol.maxConsecutiveOnesOptimal(nums, k))
    
    nums = [1, 0, 1, 0, 1, 1]
    k = 1
    print("Output: ", sol.maxConsecutiveOnes(nums, k))
    print("Output: ", sol.maxConsecutiveOnesOptimal(nums, k))
