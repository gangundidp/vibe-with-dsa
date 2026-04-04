class Solution:
    def coinChange(self, coins, amount):
        dp = {}

        return self.helper(coins, amount, dp)

    def helper(self, coins, rem, dp):
        if rem == 0:
            return 0

        if rem < 0:
            return -1

        if rem in dp:
            return dp[rem]

        mini = float('inf')

        # Try every coin
        for coin in coins:
            res = self.helper(coins, rem - coin, dp)

            # If result is valid
            if res >= 0 and res < mini:
                mini = 1 + res

        dp[rem] = -1 if mini == float('inf') else mini
        
        return dp[rem]


if __name__ == "__main__":
    obj = Solution()
    coins = [1, 2, 5]
    amount = 11

    print(obj.coinChange(coins, amount))
