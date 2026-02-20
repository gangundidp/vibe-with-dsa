class Solution:
    def nextGreaterElement(self, nums):
        st = []
        
        n = len(nums)
        ans = [0] * n
        
        for i in range(n - 1, -1, -1):
            
            # pop all smaller or equal elements
            while st and st[-1] <= nums[i]:
                st.pop()
               
            if not st:
                ans[i] = -1
            else:
                ans[i] = st[-1]   
             
            st.append(nums[i])
            
        return ans
    
if __name__ == "__main__":
    sols = Solution()
    
    arr = [1, 3, 2, 4]
    print("Output: ", sols.nextGreaterElement(arr)) # [3, 4, 4, -1]