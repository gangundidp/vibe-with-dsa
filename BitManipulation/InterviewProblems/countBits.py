class Solution:
    def minBitsFlip(self, start, goal):
        num = start ^ goal
        
        count = 0

        for i in range(32):
            # Update count if the 
            # rightmost bit is set
            count += (num & 1)
            
            # Shift the number every
            # time by 1 place
            num = num >> 1
        
        return count

if __name__ == "__main__":
    start, goal = 10, 7
    
    sol = Solution()
    ans = sol.minBitsFlip(start, goal)
    
    print("The minimum bit flips to convert number is:", ans)
