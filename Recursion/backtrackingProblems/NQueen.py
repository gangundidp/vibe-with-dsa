class Solution:
    def solve(self, col, board, n, leftRow, upperDiagonal, lowerDiagonal, ans):
        # If all queens are placed
        if col == n:
            ans.append(["".join(row) for row in board])
            return

        # Try placing queen in each row
        for row in range(n):
            # Check if safe
            if (leftRow[row] == 0 and
                lowerDiagonal[row + col] == 0 and
                upperDiagonal[n - 1 + col - row] == 0):

                # Place queen
                board[row][col] = 'Q'
                leftRow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1

                # Recurse to next column
                self.solve(col + 1, board, n,
                           leftRow, upperDiagonal, lowerDiagonal, ans)

                # Backtrack
                board[row][col] = '.'
                leftRow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n):
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        leftRow = [0] * n
        upperDiagonal = [0] * (2 * n - 1)
        lowerDiagonal = [0] * (2 * n - 1)

        self.solve(0, board, n, leftRow, upperDiagonal, lowerDiagonal, ans)
        return ans


if __name__ == "__main__":
    obj = Solution()
    n = 4
    result = obj.solveNQueens(n)

    for board in result:
        for row in board:
            print(row)
        print()
