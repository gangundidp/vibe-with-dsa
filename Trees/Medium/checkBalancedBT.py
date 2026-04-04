from maxDepthOfTree import MaximunDepth

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
class Solution:
    def isBalancedBT(self, root):
        if not root:
            return True
        
        diff = abs(MaximunDepth.maxDepthBFS(self, root.left) - MaximunDepth.maxDepthBFS(self, root.right))
        if diff > 1:
            return False
        self.isBalancedBT(root.left)
        self.isBalancedBT(root.right)
        
        return True
    
    def isBalanced(self, root):
        # If the tree is empty, it's balanced
        if root is None:
            return True

        # Calculate the height of left and right subtrees
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        # Check if the absolute difference in heights of left and right subtrees is <= 1
        if abs(leftHeight - rightHeight) <= 1 and \
            self.isBalanced(root.left) and \
            self.isBalanced(root.right):
            return True

        # If any condition fails, the tree is unbalanced
        return False
    
    def getHeight(self, root):
        # Base case: if the current node is NULL, return 0 (height of an empty tree)
        if root is None:
            return 0

        # Recursively calculate the height of left and right subtrees
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        # Return the maximum height of left and right subtrees plus 1 (for the current node)
        return max(leftHeight, rightHeight) + 1
    
    def isBalancedOptimal(self, root):
        return self.dfsHeight(root) != -1
    
    def dfsHeight(self, root):
        if root is None:
            return 0
        
        leftHeight = self.dfsHeight(root.left)
        if leftHeight == -1:
            return -1
        
        rightHeight = self.dfsHeight(root.right)
        if rightHeight == -1:
            return -1
        
        if abs(leftHeight - rightHeight) > 1:
            return -1
        
        return max(leftHeight, rightHeight) + 1
        

        
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)
    
    sols = Solution()
    
    print("Is Balanced Tree: ", sols.isBalancedBT(root))
    print("Is Balanced Tree: ", sols.isBalancedOptimal(root))
        
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(5)
    root.left.right = Node(4)
        
    print("Is Balanced Tree: ", sols.isBalancedBT(root))
    print("Is Balanced Tree: ", sols.isBalancedOptimal(root))
        
        
