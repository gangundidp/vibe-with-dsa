'''
Problem Statement: Given the head of a linked list and an integer value, find out whether
the integer is present in the linked list or not. Return true if it is present, or else return false.

Examples
Input: 0->1->2, val = 2
Output: True
Explanation: Since element 2 is present in the list, return true.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
class Solution:
    def findElement(self, head, val):
        temp = head
        
        while temp is not None:
            if temp.data == val:
                return True
            temp = temp.next
        return False
    
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
    head.next.next = Node(3)
    
    print('Linked List: ', end='')
    sols.printList(head)

    print(sols.findElement(head, 2))
    print(sols.findElement(head, 7))