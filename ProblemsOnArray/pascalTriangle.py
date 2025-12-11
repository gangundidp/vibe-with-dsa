class Solution:
    # Given row & column, find the element at the place.
    def funcNcR(self, n, r):
        res = 1
        for i in range(r):
            res = res * (n-i)
            res = res / (i + 1)
        return res
    
    # Print N-th row
    def printRow(self, row):
        for r in range(1, row+1):
            print(self.funcNcR(row-1, r-1))
            
    # Print Entire Triangle
    def generateRow(self, row):
        ans = 1
        ansrow = [1]
        for col in range(1, row):
            ans = ans * (row - col)
            ans //= col
            ansrow.append(ans)
        return ansrow

    def pascalTriangle(self, n):
        ans = []
        for row in range(1, n+1):
            ans.append(self.generateRow(row))
        return ans
    
if __name__ == "__main__":
    # row = int(input("Row: "))
    # col = int(input("Col: "))
    sols = Solution()
    # print(f"{row}-th {col}-th element: {sols.funcNcR(row-1, col-1)}")
    # nthRow = int(input('Nth row: '))
    # print(f"Nth Row: ", end=" ")
    # sols.printRow(nthRow)
    no_of_rows = int(input("Enter no of rows: "))
    ans = sols.pascalTriangle(no_of_rows)
    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()