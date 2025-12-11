from array import array as arr
from typing import *

class Solution:
    '''
    Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    '''
    
    def stockBuySell(self, nums: List[int]) -> int:
        maxProfit = 0
        buy_day = sell_day = -1
        for i in range(len(nums)):
            profit = 0
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    profit = nums[j] - nums[i]
                if profit > maxProfit:
                    maxProfit = profit
                    buy_day, sell_day = i, j
                    
        return maxProfit, (buy_day+1, sell_day+1)

    def stockBuySellOptimal(self, nums: List[int]) -> int:
        '''
        Algorithm
        The idea is to track the minimum price so far while traversing the array and calculate the profit if we sold today. This way, we can constantly update the maximum profit without using nested loops. We’re basically simulating:
        What’s the lowest price we’ve seen so far?
        What’s the profit if we sold today?
        Is it better than our best so far?
        Initialize a variable to store the minimum price so far, set it to a very large value initially.
        Initialize a variable to store the maximum profit seen so far, set it to 0 initially.
        Loop through each price in the array.
        Update the minimum price if the current price is smaller.
        Calculate the profit if the stock were bought at the minimum price and sold at the current price.
        Update the maximum profit if this new profit is higher.
        Return the maximum profit after the loop ends.
        '''
        maxProfit = 0
        profit = 0
        minBuy = float('inf')
        for i in range(len(nums)):
            if nums[i] < minBuy:
                minBuy = nums[i]
            else:
                profit = nums[i] - minBuy
                
            if profit > maxProfit:
                maxProfit = profit
                
        return maxProfit
    
if __name__ == "__main__":
    sols = Solution()
    nums = arr('i', [7,1,5,3,6,4])
    # nums = arr('i', [7,6,4,3,1])
    print('Maximum profit: ', sols.stockBuySell(nums))
    print('Maximum profit: ', sols.stockBuySellOptimal(nums))