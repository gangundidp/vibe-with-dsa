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
    
    def preOrder(self, root, arr):
        if root is None:
            return
        
        arr.append(root.data)
        
        self.preOrder(root.left, arr)
        
        self.preOrder(root.right, arr)
        
        
    def iterativePreOrder(self, root):
        ans, st = [], []
            
        if not root:
            return ans
            
        st.append(root)
            
        while st:
            node = st.pop()
                
            ans.append(node.data)
                
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
                    
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
    sols.preOrder(root, arr)
    
    print("Pre-order Traversal: ", arr)
    print("Iterative Pre-order Traversal: ", sols.iterativePreOrder(root))
    