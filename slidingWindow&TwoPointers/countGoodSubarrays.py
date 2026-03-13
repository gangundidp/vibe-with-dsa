class Solution:
    def countGoodSubarraysBrute(self, nums, k):
        res = 0
        
        for i in range(len(nums)):
            hash_set = set()
            # temp_list = []
            
            for j in range(i, len(nums)):
                if len(hash_set) <= k:
                    hash_set.add(nums[j])

                # if nums[j] not in hash_set:
                #     temp_list.append(nums[j])

                if len(hash_set) == k:
                    # res.append(temp_list) # wrong
                    res += 1
                    
        # return len(res)
        return res
    
    def countGoodSubarrays(self, nums, k):
        return self.countAtMost(nums, k) - self.countAtMost(nums, k - 1)
    
    def countAtMost(self, nums, k):
        count = 0
        
        left = 0
        freq = {}
        for right in range(len(nums)):
            if nums[right] not in freq or freq[nums[right]] == 0:
                k -= 1
            
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # if len(freq) <= k:
            #     k -= 1
            
                
            while k < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    k += 1
                    # del freq[nums[left]] 
                left += 1

            count += right - left + 1
                
        return count
    
if __name__ == "__main__":
    sols = Solution()
    nums = [1, 2, 1, 2, 3]
    k = 2
    print("Output: ", sols.countGoodSubarraysBrute(nums, k))
    print("Output: ", sols.countGoodSubarrays(nums, k))

    nums = [1, 2, 1, 3, 4]
    k = 3
    print("Output: ", sols.countGoodSubarraysBrute(nums, k))
    print("Output: ", sols.countGoodSubarrays(nums, k))