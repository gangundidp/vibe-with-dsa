class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # Global variable
        self.diameter = 0  

    def calculateHeight(self, node):
        if node is None:
            return 0

        leftHeight = self.calculateHeight(node.left)
        rightHeight = self.calculateHeight(node.right)

        # Calculate the diameter at the current node and update the global variable
        self.diameter = max(self.diameter, leftHeight + rightHeight)

        # Return the height of the current subtree
        return 1 + max(leftHeight, rightHeight)


    def diameterOfBinaryTree(self, root):
        self.calculateHeight(root)

        # Return the maximum diameter found during traversal
        return self.diameter

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    sols = Solution()
    diameter = sols.diameterOfBinaryTree(root)

    print("The diameter of the binary tree is:", diameter)

                                