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
    
    def postOrder(self, root, arr):
        if root is None:
            return
        
        
        self.postOrder(root.left, arr)
        self.postOrder(root.right, arr)
        arr.append(root.data)
        
    def iterativePostOrder(self, root):
        ans, st, st2 = [], [], []
        
        if not root:
            return ans
        
        st.append(root)
                
        while st:
            node = st.pop()
            st2.append(node)
                
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
                
        while st2:
            ans.append(st2.pop().data)
            
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
    sols.postOrder(root, arr)
    
    print("Post-order Traversal: ", arr)
    print("Iterative Post-order Traversal: ", sols.iterativePostOrder(root))
    