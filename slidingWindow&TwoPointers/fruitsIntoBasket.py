from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        n = len(fruits)
        max_fruits = 0
        
        for i in range(n):
            basket = set()
            for j in range(i, n):
                if fruits[j] not in basket:
                    basket.add(fruits[j])
                
                if len(basket) > 2:
                    break
                
                curr_count = j - i + 1
                max_fruits = max(max_fruits, curr_count)

        return max_fruits
    
    def totalFruitsBetter(self, fruits):
        n = len(fruits)
        max_fruits = 0
        basket = defaultdict(int)
        
        l, r = 0, 0
        
        while r < n:
            basket[fruits[r]] += 1
            
            # If more than 2 types, shrink window from left
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
                
            curr_count = r - l + 1
            max_fruits = max(max_fruits, curr_count)
            r += 1
        
        return max_fruits
            
    def totalFruitsOptimal(self, fruits):
        n = len(fruits)
        basket = defaultdict(int)
        max_fruits = 0
        
        l, r = 0, 0
        while r < n:
            basket[fruits[r]] += 1
            
            if len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
                
            max_fruits = max(max_fruits, r - l + 1)
            r += 1
        
        return max_fruits
                    
            
if __name__ == "__main__":
    sol = Solution()
    fruits = [1,2,1,2,3]
    print("Output: ", sol.totalFruit(fruits))
    print("Output: ", sol.totalFruitsBetter(fruits))
    print("Output: ", sol.totalFruitsOptimal(fruits))
    
    fruits = [1, 2, 3, 2, 2, 3, 1]
    print("Output: ", sol.totalFruit(fruits))
    print("Output: ", sol.totalFruitsBetter(fruits))
    print("Output: ", sol.totalFruitsOptimal(fruits))
