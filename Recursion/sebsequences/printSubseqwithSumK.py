class Solution:
    # Print only one subsequece with sum k
    def printSubseqwithSumK(self, nums, k):
        res = []
        if (self.findSubseq(0, nums, res, 0, k)):
            return res
        return "No subsequeces with sum K"
    
    def findSubseq(self, idx, nums, res, sum, k):
        if idx == len(nums):
            if sum == k:
                return True
            return False
        
        res.append(nums[idx])
        if (self.findSubseq(idx + 1, nums, res, sum + nums[idx], k)):
            return True
        
        res.pop()
        if (self.findSubseq(idx + 1, nums, res, sum, k)):
            return True
        
        return False
    
if __name__ == "__main__":
    sols = Solution()
    
    nums = [1, 2, 1]
    print("Output: ", sols.printSubseqwithSumK(nums, 2))
        
        