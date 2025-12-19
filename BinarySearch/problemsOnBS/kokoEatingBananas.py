from array import array as arr
from typing import *
from math import ceil

class Solution:
    def kokoEatingBananas(self, piles_of_bananas: List[int], hours: int) -> int:
        n = len(piles_of_bananas)
        max_pile = max(piles_of_bananas)
        min_bananas_to_be_eaten = 0
        
        for i in range(1, max_pile+1):
            sum = 0
            for pile in piles_of_bananas:
                time_taken = ceil(pile/i)
                # print(time_taken)
                sum += time_taken
                
            # print(sum)
            if sum <= hours:
                return i
        return max_pile
    
    def checkTotalHours(self, piles_of_bananas: List[int], no_of_bananas_to_be_eaten_per_hour: int) -> int:
        total_hours = 0
        
        for pile in piles_of_bananas:
            total_hours += ceil(pile / no_of_bananas_to_be_eaten_per_hour)

        return total_hours
    
    def findMinBananasEaten(self, piles_of_bananas: List[int], hours: int) -> int:
        max_pile = max(piles_of_bananas)
        n = len(piles_of_bananas)
    
        if (n == hours):
            return max_pile
    
        low, high = 1, max_pile
        ans = 0
        
        while (low <= high):
            mid = (low + high)//2
            
            taken_hours = self.checkTotalHours(piles_of_bananas, mid)
            
            if taken_hours <= hours:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
                
    
if __name__ == "__main__":
    sols = Solution()
    piles_of_bananas = arr('i', [7, 15, 6, 3])
    print('Output: ', sols.kokoEatingBananas(piles_of_bananas, 8))
    piles_of_bananas = arr('i', [25, 12, 8, 14, 19])
    print('Output: ', sols.kokoEatingBananas(piles_of_bananas, 5))
    
    piles_of_bananas = arr('i', [7, 15, 6, 3])
    print('Output: ', sols.findMinBananasEaten(piles_of_bananas, 8))
    piles_of_bananas = arr('i', [25, 12, 8, 14, 19])
    print('Output: ', sols.findMinBananasEaten(piles_of_bananas, 5))