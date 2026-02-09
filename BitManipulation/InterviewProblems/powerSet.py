class Solution:
    '''
    To solve it using bit wise operators, we observe a pattern that the number of subsets is dependant on the size of the input array as:
    N = 1, No. of subsets = 2
    N = 2, No. of subsets = 4
    N = 3, No. of subsets = 8 and so on…
    No. of subsets of input array of size N = 2N = [1 << n]
    
    index=  0  1  2
    nums = [5, 7, 8]

        i=2 1 0
        - - - - - - - -    
        | 0 0 0 -> []
        | 0 0 1 -> [5]
        | 0 1 0 -> [7]
        | 0 1 1 -> [5 7]
        | 1 0 0 -> [8]
        | 1 0 1 -> [5, 8]
        | 1 1 0 -> [7, 8]
        | 1 1 1 -> [5, 7, 8]
    '''
    def getPowerSet(self, nums):
        n = len(nums)

        no_of_subsets = 1 << n

        ans = []
        for i in range(no_of_subsets):
            subset = []

            for j in range(n):
                if (i & (1<<j)):
                    subset.append(nums[j])
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
        
'''
Time Complexity: O(N x 2N) where N is the number of elements in the input array. Iterating through 
    all possible numbers from 0 to 2N-1 where N is the number of elements in the input array requires 
    O(2N) iterations.For each iteration, we perform O(N) operations to construct the corresponding subset 
    by interpreting the bits of the number.

Space Complexity: O(N x 2N) where N is the number of elements in the input array. We store all subsets 
    in a list. Since there are 2N subsets in the power set, each subset can have at most N elements.
'''
