class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    """
    Pre-order: Preorder traversal is a depth-first search (DFS) method for binary trees that visits nodes in a Root -> Left -> Right order.
    In-order: LeetCode) Binary Tree Inorder Traversal: 2 Approaches ...Inorder traversal is a depth-first algorithm that visits binary tree nodes in a Left-Root-Right order.
    Post-order: A Comprehensive Guide to Binary Tree Traversal in Java | by ...Postorder traversal is a depth-first search (DFS) technique for binary trees that visits nodes in a Left -> Right -> Root order.
    """
    def preInPostOrderTraversal(self, root):
        pre, ino, post = [], [], []
        
        # If the tree is empty, return empty traversals
        if root is None:
            return []
        
        st = [(root, 1)]
        
        while st:
            node, state = st.pop()
            
            if state == 1:
                # Store the node's data in the preorder traversal
                pre.append(node.data)
                # Move to state 2 (inorder) for this node
                st.append((node, 2))
                 # Push left child onto the stack for processing
                if node.left:
                    st.append((node.left, 1))
                    
            elif state == 2:
                 # Store the node's data in the inorder traversal
                ino.append(node.data)
                # Move to state 3 (postorder) for this node
                st.append((node, 3))
                # Push right child onto the stack for processing
                if node.right:
                    st.append((node.right, 1))
                    
            else:
                # Store the node's data in the postorder traversal
                post.append(node.data)
                
        return [pre, ino, post]
    
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    
    sols = Solution()
    
    traversals = sols.preInPostOrderTraversal(root)
    
    pre = traversals[0]
    ino = traversals[1]
    post = traversals[2]

    print("Pre-order Traversal: ", pre)
    print("In-order Traversal: ", ino)
    print("Post-order Traversal: ", post)
        
        
        
        