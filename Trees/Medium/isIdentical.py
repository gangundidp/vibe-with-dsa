class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isIdentical(self, node1, node2):
        # Case 1: If both nodes are NULL, they are identical
        if node1 is None and node2 is None:
            return True

        # Case 2: If only one of the nodes is NULL, they are not identical
        if node1 is None or node2 is None:
            return False

        return (node1.data == node2.data) and self.isIdentical(node1.left, node2.left) and self.isIdentical(node1.right, node2.right)

if __name__ == "__main__":
    # First binary tree (Node 1)
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)

    # Second binary tree (Node2)
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)

    sols = Solution()

    print("The binary trees are identical. ", sols.isIdentical(root1, root2))

    # First binary tree (Node 1)
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)

    # Second binary tree (Node2)
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(5)

    sols = Solution()

    print("The binary trees are identical. ", sols.isIdentical(root1, root2))

