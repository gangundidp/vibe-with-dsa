class Solution:
    def countAtMost(self, nums, k):
        left = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                k -= 1

            # Shrink the window while k < 0
            while k < 0:
                if nums[left] % 2 != 0:
                    k += 1
                left += 1

            res += (right - left + 1)

        return res

    def numberOfSubarrays(self, nums, k):
        return self.countAtMost(nums, k) - self.countAtMost(nums, k - 1)

if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    k = 3
    sol = Solution()
    print("Output: ", sol.numberOfSubarrays(nums, k))
