class Solution:
    def totalFruit(self, fruits):
        max_len = 0
        last_fruit = second_last_fruit = -1
        curr_count = 0
        lastfruit_streak = 0

        for fruit in fruits:
            
            if fruit == last_fruit or fruit == second_last_fruit:
                curr_count += 1
            else:
                curr_count = lastfruit_streak + 1

            if fruit == last_fruit:
                lastfruit_streak += 1
            else:
                lastfruit_streak = 1
                second_last_fruit = last_fruit
                last_fruit = fruit

            max_len = max(max_len, curr_count)

        return max_len

if __name__ == "__main__":
    sol = Solution()
    fruits = [1,2,1,2,3]
    print("Output: ", sol.totalFruit(fruits))
