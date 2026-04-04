class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
class Solution:
    '''
                    4
            5               6
        3       2       7       8     
    1                9      
    
    '''
    
    def inOrder(self, root, arr):
        if root is None:
            return
        
        
        self.inOrder(root.left, arr)
        arr.append(root.data)
        
        self.inOrder(root.right, arr)
        
    def iterativeInorder(self, root):
        ans, st = [], []
        
        if not root:
            return ans
        
        node = root
                
        while True:
            if node is not None:
                st.append(node)
                node = node.left
                
            else:
                if not st:
                    break
                
                node = st.pop()
                
                ans.append(node.data)
                
                node = node.right
                
        return ans


        
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.left.left.left = Node(1)
    root.right.left = Node(7)
    root.right.left.left = Node(9)
    root.right.right = Node(8)
    
    sols = Solution()
    arr = []
    sols.inOrder(root, arr)
    
    print("In-order Traversal: ", arr)
    print("Iterative In-order Traversal: ", sols.iterativeInorder(root))
    