class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, idx):
            if idx == len(word):
                return True

            if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = '#'

            found = (dfs(i + 1, j, idx + 1) or
                     dfs(i - 1, j, idx + 1) or
                     dfs(i, j + 1, idx + 1) or
                     dfs(i, j - 1, idx + 1))

            board[i][j] = temp

            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False


if __name__ == "__main__":
    sol = Solution()
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    print(sol.exist(board, "ABCCED"))  # True
    print(sol.exist(board, "SEE"))     # True
    print(sol.exist(board, "ABCB"))    # False
