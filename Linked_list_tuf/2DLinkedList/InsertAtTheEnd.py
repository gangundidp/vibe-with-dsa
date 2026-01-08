'''
Problem Statement: Given a doubly linked list, and a value ‘k’, insert a node having value 
‘k’ at the end of the doubly linked list.

Examples
Example 1:
Input Format:
  
DLL: 1 <-> 2 <-> 3 <-> 4  
Value to be Inserted: 6  
Result:
  DLL: 1 <-> 2 <-> 3 <-> 4 <-> 6  
Explanation:
  A new node with value 6 has been inserted at the end of the doubly linked list after the tail node.

'''

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class Solution:
    def insertAtTheEnd(self, head, value):
        temp = head
        
        while temp.next.next is not None:
            temp = temp.next
        
        temp.next.next = Node(value, temp.next)
        
    def printList(self, head):
        temp = head
        while temp:
            print(temp.data, end='<->')
            temp = temp.next
        print(None)

if __name__ == "__main__":
    sols = Solution()
    
    head = Node(1)
    head.prev = None
    head.next = Node(2)
    head.next.prev = head

    print('Original List: ', end='')
    sols.printList(head)

    sols.insertAtTheEnd(head, 3)
    print('After insertion: ', end='')
    sols.printList(head)