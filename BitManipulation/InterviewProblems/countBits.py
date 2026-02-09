class Solution:
    '''
    Problem Statement: Given two integers start and goal. Flip the minimum number of bits of start integer to convert it into goal integer.

    A bits flip in the number val is to choose any bit in binary representation of val and flipping it from either 0 to 1 or 1 to 0.
    '''
    
    def minBitsFlip(self, start, goal):
        xorNum = start ^ goal
        
        cnt = 0
        while xorNum:
            cnt += (xorNum & 1)
            xorNum >>= 1
            
        return cnt

if __name__ == "__main__":
    start, goal = 10, 7
    # start, goal = 5, 1
    # start, goal = 3, 4
    
    sol = Solution()
    ans = sol.minBitsFlip(start, goal)
    
    print("The minimum bit flips to convert number is:", ans)
