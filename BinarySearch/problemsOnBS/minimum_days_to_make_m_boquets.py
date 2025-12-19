from array import array as arr
from typing import *

class Solution:
    '''
    Problem Statement: You are given 'N’ roses and you are also given an array 'arr' where 'arr[i]' denotes that the 'ith' rose will bloom on the 'arr[i]th' day. You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly 'k' adjacent bloomed roses to make a single bouquet. Find the minimum number of days required to make at least ‘m' bouquets each containing 'k' roses. Return -1 if it is not possible.

    Examples
    Example 1:
    Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
    Result: 12
    Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed. So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.

    Example 2:
    Input Format: N = 5, arr[] = {1, 10, 3, 10, 2}, m = 3, k = 2
    Result: -1
    Explanation: If we want to make 3 bouquets of 2 flowers each, we need at least 6 flowers. But we are given only 5 flowers, so, we cannot make the bouquets.

    '''
    def findMinDays(self, bloom_days_list: List[int], day: int, k: int) -> int:
        no_of_roses, no_of_bouquets = 0, 0
        for i in bloom_days_list:
            if i <= day:
                no_of_roses += 1
            else:
                no_of_roses = 0

            if no_of_roses == k:
                no_of_bouquets += 1
                no_of_roses = 0
                
        return no_of_bouquets
    
    def minDaysToMakeMBouquets(self, bloom_days_list: List[int], m: int, k: int) -> int:
        '''
            Algorithm
            -> If the total number of flowers required to make all bouquets is more than the flowers available, it is not possible to make the bouquets. So, return -1.
            -> Loop through each day starting from the earliest bloom day to the latest bloom day to test all possible answers.
            -> For each day, check if it's possible to make the required number of bouquets using the flowers that have bloomed by that day. If yes, return that day as the answer.
            -> If no suitable day is found after checking all possibilities, it means it's impossible to make the bouquets. So, return -1.
        '''
        n = len(bloom_days_list)
        min_day, max_day = min(bloom_days_list), max(bloom_days_list)
        min_no_of_days = float('inf')
        
        if (m * k > n):
            return -1
        
        for day in range(min_day, max_day + 1):
            no_of_bouquets = self.findMinDays(bloom_days_list, day, k)
                
            if no_of_bouquets == m and min_no_of_days > day:
                min_no_of_days = day
                
        return min_no_of_days
    
    
    def findMinDaysUsingBs(self, bloom_days_list: List[int], day: int, m:int,  k: int) -> bool:
        no_of_roses, no_of_bouquets = 0, 0
        
        for i in bloom_days_list:
            if i <= day:
                no_of_roses += 1
            else:
                no_of_roses = 0
            
            if no_of_roses == k:
                no_of_bouquets += 1
                no_of_roses = 0
                
        return no_of_bouquets >= m
        
    def minDaysToMakeMBouquetsUsingBS(self, bloom_days_list: List[int], m: int, k: int) -> int:
        n = len(bloom_days_list)
        low, high = min(bloom_days_list), max(bloom_days_list)
        ans = -1
        
        if (m * k > n):
            return -1

        while (low <= high):
            mid = (low + high)//2
            
            if (self.findMinDaysUsingBs(bloom_days_list, mid, m, k)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
            
            
            

if __name__ == "__main__":
    sols = Solution()
    bloom_days_list = arr('i', [7, 7, 7, 7, 13, 11, 12, 7])
    print('Output: ', sols.minDaysToMakeMBouquets(bloom_days_list, 2, 3))
    bloom_days_list = arr('i', [1, 10, 3, 10, 2])
    print('Output: ', sols.minDaysToMakeMBouquets(bloom_days_list, 3, 2))
            
    bloom_days_list = arr('i', [7, 7, 7, 7, 13, 11, 12, 7])
    print('Output: ', sols.minDaysToMakeMBouquetsUsingBS(bloom_days_list, 2, 3))
    bloom_days_list = arr('i', [1, 10, 3, 10, 2])
    print('Output: ', sols.minDaysToMakeMBouquetsUsingBS(bloom_days_list, 3, 2))
            
        
        
        
        
    