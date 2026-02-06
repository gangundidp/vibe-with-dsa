class Solution:

    def singleNumber(self, nums):
        n = len(nums)
        XOR = 0
        
        for i in range(n):
            XOR = XOR ^ nums[i]

        rightmost = (XOR & (XOR - 1)) ^ XOR
        
        XOR1, XOR2 = 0, 0
        
        for i in range(n):
            if nums[i] & rightmost:
                XOR1 = XOR1 ^ nums[i]
            else:
                XOR2 = XOR2 ^ nums[i]
        
        # Return the result in sorted order
        return [XOR1, XOR2] if XOR1 < XOR2 else [XOR2, XOR1]


nums = [1, 2, 1, 3, 5, 2]
sol = Solution()
ans = sol.singleNumber(nums)

print("The single numbers in given array are:", ans[0], "and", ans[1])