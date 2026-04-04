from collections import deque

class Node:
    def __init__(self, val):
         self.data = val
         self.left = None
         self.right = None
         
class MaximunDepth:
    '''
                    1
                  /   \
                 2     5
                     /   \
                    4     6
                   /
                  5  
    '''
    # Doubt
    """
    def maxDepthDFS(self, root):
        st = []
        ans = []
        maxi = 0
        
        if not root:
            return maxi
        
        node =  root
        count = 0   
        while True:
            count += 1
            if node is not None:
                st.append(node)
                node = node.left
            else:
                if not st:
                    break
                
                maxi = max(maxi, count)
                count = 0
                node = st.pop()
                # ans.append(node.data)
                node = node.right
                
        # return ans, maxi
        return maxi
        """

    
    def maxDepthBFS(self, root):
        if not root:
            return 0
        que = deque([root])
        level = 0
        while que:
            level += 1
            for _ in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
        return level
            
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.right.left = Node(4)
    root.right.right = Node(6)
    root.right.left.left = Node(5)

    sols = MaximunDepth()
    
    print("Maximum Depth of the Tree: ", sols.maxDepthBFS(root))
    # print("Maximum Depth of the Tree: ", sols.maxDepthDFS(root))
    
    
    '''
                    4
                  /   \
                 6     7
                /  \      \
               8    9      3  
                     \
                      10
                    /
                   2 
    '''
    
    root = Node(4)
    root.left = Node(6)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(9)
    root.left.right.right = Node(10)
    root.left.right.right.left = Node(2)
    root.right.right = Node(3)

    sols = MaximunDepth()
    
    print("Maximum Depth of the Tree: ", sols.maxDepthBFS(root))
    # print("Maximum Depth of the Tree: ", sols.maxDepthDFS(root))
    