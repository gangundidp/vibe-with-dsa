'''
Problem Statement: Given a Linked List, delete the tail of the list and print the updated list.

Examples
Input: 0->1->2
Output: 0->1
Explanation: Last node of the Linked List is 2.

'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Solution:
    def deleteTail(self, head):
        # If list is empty or has one node
        if head is None or head.next is None:
            return None
        
        curr = head
        while curr.next.next is not None:
            curr = curr.next
            
        curr.next = None
        
        return head
    
    def printList(self, head):
        temp = head
        
        while temp:
            print(temp.data, end='->')
            temp = temp.next
        print(None)

if __name__ == "__main__":
    sols = Solution()

    head = Node(1)
    head.next = Node(2)

    print('Original List: ')
    sols.printList(head)
    
    sols.deleteTail(head)
    print('List after deleting tail: ')
    sols.printList(head)

    
            
        