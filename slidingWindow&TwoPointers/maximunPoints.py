class Solution:
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
    print("Output: ", sol.maxScore(cards, k))
