from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        ans = []
        
        if root is None:
            return ans
        
        que = deque([root])

        while que:
            level = []
            for _ in range(len(que)):
                node = que.popleft()
                
                level.append(node.data)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
            ans.append(level)
            
        return ans
    
if  __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    sols = Solution()
    print("Level Ordered Traversal: ", sols.levelOrder(root))
    
    
        
        