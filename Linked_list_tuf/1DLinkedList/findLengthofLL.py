'''
Problem Statement: Given the head of a linked list, print the length of the linked list.

Examples
Input: 0->1->2 
Output: 3
Explanation: The list has a total of 3 nodes, thus the length of the list is 3.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def findLengthOfLinkedList(self, head):
        temp = head
        cnt = 0
        
        while temp:
            cnt += 1
            temp = temp.next
        
        return cnt
    
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

    print('Linked List: ', sols.printList(head))
    print('Length of Linked List: ', sols.findLengthOfLinkedList(head))
    