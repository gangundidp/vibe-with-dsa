class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    
class Solution:
    def reverseLL(self, head):
        stack = []
        temp = head
        while temp:
            stack.append(temp.data)
            temp = temp.next
            
        temp = head
        while temp:
            temp.data = stack.pop()
            temp = temp.next
        
        return head

    def reverseLlOptima(self, head):
        temp = head
        
        prev = None
        while temp is not None and temp.next is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        temp.next = prev
        return temp
    
    def recursiveReverse(self, head):

        if (head is None or head.next is None):
            return head
        newHead = self.recursiveReverse(head.next)
        front = head.next
        front.next = head
        head.next = None
    
        return newHead

    def printLL(self, head):
        while head:
            print(head.data, end='->')
            head = head.next
        print(None)
    
if __name__ == "__main__":
    sols = Solution()
    
    head = Node(1, Node(2, Node(3, Node(4))))

    sols.printLL(head)
    head = sols.reverseLL(head)
    sols.printLL(head)
    
    head = Node(1, Node(2, Node(3, Node(4))))

    sols.printLL(head)
    head = sols.reverseLlOptima(head)
    sols.printLL(head)
            
    head = Node(1, Node(2, Node(3, Node(4))))

    sols.printLL(head)
    head = sols.recursiveReverse(head)
    sols.printLL(head)
            