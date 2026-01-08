'''
Problem Statement: Given a Doubly Linked List, delete the last node of the Doubly Linked List.

Examples
Input:  DLL: 1 <-> 3 <-> 4 <-> 1
Output: DLL: 1 <-> 3 <-> 4
Explanation: Last node of the Doubly Linked List to be deleted is 1.

'''

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Solution:
    def deleteTail(self, head):
        temp = head
        
        while temp.next:
            temp = temp.next
        
        temp.prev.next = None
        
    def printList(self, head):
        while head:
            print(head.data, end='<->')
            head = head.next
        print(None)
    
if __name__ == "__main__":
    sols = Solution()
    
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    
    print('Original List: ', end='')
    sols.printList(head)
    
    sols.deleteTail(head)

    print('List After deletion: ', end='')
    sols.printList(head)
    