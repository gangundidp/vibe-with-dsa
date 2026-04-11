class Solution:
    def houseRobberRecursive(self, arr, n):
        dp = [0] * (n+1)
        dp[0] = arr[0]
        
        for i in range(len(arr)):
            pick = arr[i]
            if i > 1:
                pick += dp[i - 2]
            not_pick = 0 + dp[i - 1]

            dp[i] = max(pick, not_pick)

        return dp[n]
    
    def main(self, arr):
        n = len(arr) - 1
        temp1, temp2 = [], []
        for i in range(n):
            temp1.append(arr[i])
            
        for i in range(1, n+1):
            temp2.append(arr[i])
            
        return max(self.houseRobberRecursive(temp1, len(temp1) - 1), self.houseRobberRecursive(temp2, len(temp2) - 1))
        
        
        
if __name__ == "__main__":
    sols = Solution()
    arr = [2, 1, 4, 9] # 10
    print("Output: ", sols.main(arr)) 
    
    arr = [1, 5, 2, 1, 6] # 11
    print("Output: ", sols.main(arr))
    
    arr = [5, 2, 1, 6, 1] # 11
    print("Output: ", sols.main(arr))
    