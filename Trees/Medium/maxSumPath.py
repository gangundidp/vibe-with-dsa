class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
class Solution:
    def maxSumPath(self, root):
        self.max_sum = float("-inf")
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        if not node:
            return 0
        
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))


        self.max_sum = max(self.max_sum, left + right + node.data)
        
        return max(left, right) + node.data
    

if __name__ == "__main__":
    root = Node(-10)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    sols = Solution()
    print("Maximum Sum: ", sols.maxSumPath(root))