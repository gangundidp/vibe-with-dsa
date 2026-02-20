class Solution:
    '''
    
    Problem Statement: Given an array of integers arr, your task is to find the Next Smaller Element (NSE) for every element in the array.
        The Next Smaller Element for an element x is defined as the first element to the right of x that is smaller than x.
        If there is no smaller element to the right, then the NSE is -1.
    
    Algorithm
        Initialize an answer array filled with -1
        Initialize an empty stack
        Loop from i = n - 1 to 0
        While stack is not empty and top is greater than or equal to current element, pop the stack
        If stack is not empty, set answer[i] to top of stack
        Push current element to stack
        Return the answer array
    
    '''
    def nextSmallerElement(self, nums):
        st = []
        
        n = len(nums)
        ans = [-1] * n
        
        for i in range(n-1, -1, -1):
            while st and st[-1] >= nums[i]:
                st.pop()
                
            if st:
                ans[i] = st[-1]
            
            st.append(nums[i])
        return ans
    
if __name__ == "__main__":
    sols = Solution()
    
    nums = [4, 8, 5, 2, 25]
    print("Output: ", sols.nextSmallerElement(nums))