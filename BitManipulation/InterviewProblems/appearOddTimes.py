class Solution:
    def singleNumber(self, nums):
        XOR = 0

        for num in nums:
            XOR ^= num
        
        return XOR

if __name__ == "__main__":
    nums = [1, 2, 2, 4, 3, 1, 4]
    
    sol = Solution()
    ans = sol.singleNumber(nums)
    
    print(f"The single number in given array is: {ans}")