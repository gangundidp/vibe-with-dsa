class Solution:
    def maxScoreBrute(self, cardPoints, k):
        maxTotal = 0
        n = len(cardPoints)

        for i in range(k + 1):
            temp_sum = 0

            for j in range(i):
                temp_sum += cardPoints[j]

            for j in range(k - i):
                temp_sum += cardPoints[n - 1 - j]

            maxTotal = max(maxTotal, temp_sum)
        
        return maxTotal
     
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)

        total = sum(cardPoints[:k])
        maxPoints = total

        for i in range(k):
            # Subtract from the front
            total -= cardPoints[k - 1 - i]

            # Add from the back
            total += cardPoints[n - 1 - i]

            # Update max score
            maxPoints = max(maxPoints, total)

        return maxPoints

if __name__ == "__main__":
    cards = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    sol = Solution()
    print("Output: ", sol.maxScoreBrute(cards, k))
    print("Output: ", sol.maxScore(cards, k))

    cards = [5, 4, 1, 8, 7, 1, 3 ]
    k = 3
    sol = Solution()
    print("Output: ", sol.maxScoreBrute(cards, k))
    print("Output: ", sol.maxScore(cards, k))
    
    cards = [2, 3, 1, 4]
    k = 2
    sol = Solution()
    print("Output: ", sol.maxScoreBrute(cards, k))
    print("Output: ", sol.maxScore(cards, k))
