'''
Problem Statement: Given a linked list and an integer value val, insert a new node with that
value at the beginning (before the head) of the list and return the updated linked list.

Examples
Input: 0->1->2, val = 5 
Output: 5->0->1->2
Explanation: We need to insert the value 5 before the head of the given Linked List.

'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Solution:
    def insertAtHead(self, head, newHead):
        newNode = Node(newHead, head)
        return newNode
    
    def printList(self, head):
        temp = head
        while temp:
            print(temp.data, end='->')
            temp = temp.next
        print(None)
        
if __name__ == "__main__":
    sols = Solution()
    
    head = Node(2)
    head.next = Node(3)
    
    print('Original List: ', end=' ')
    sols.printList(head)

    head = sols.insertAtHead(head, 1) # return new head address
    print("After Insertion at head: ", end=' ')
    sols.printList(head)