class Solution:
    def getPowerSet(self, nums):
        n = len(nums)

        subsets = 1 << n
        ans = []

        for num in range(subsets):
            subset = []

            for i in range(n):
                if num & (1 << i):
                    subset.append(nums[i])

            ans.append(subset)

        return ans


if __name__ == "__main__":
    nums = [5, 7, 8]
    obj = Solution()
    subsets = obj.getPowerSet(nums)
    
    print("Initial Input Array:", nums)
    print("Subsets:")
    for subset in subsets:
        print("[", " ".join(map(str, subset)), "]")
