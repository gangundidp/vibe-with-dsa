from collections import deque

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        ans = []

        if not root:
            return ans

        q = deque([root])

        # Boolean flag to control traversal direction
        leftToRight = True

        while q:
            size = len(q)

            level = [0] * size

            for i in range(size):
                node = q.popleft()

                index = i if leftToRight else size - 1 - i
                level[index] = node.data

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Flip direction for the next level
            leftToRight = not leftToRight

            ans.append(level)

        return ans

if __name__ == "__main__":
    # Create binary tree:
    #        1
    #      /   \
    #     2     3
    #    / \     \
    #   4   5     6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    sols = Solution()
    print("Zig-Zag Traversal: ", sols.zigzagLevelOrder(root))