class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Solution:
    def detectLoop(self, head):
        map = {}
        temp = head
        while temp:
            if temp in map:
                return True
            map[temp] = 1
            temp = temp.next
        return False
    
    # Floyd's Cycle Detection Algorithm.
    def detectLoopUsingFloydsAlgo(self, head):
        fast = slow = head

        while (fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        
    
    def printLL(self, head):
        while head:
            print(head.data, end='->')
            head = head.next
        print(None)
    
if __name__ == "__main__":
    sols = Solution()
    
    head = Node(1)
    head.next = Node(2, Node(3))
    head.next.next.next = Node(4, Node(5, head.next.next))
    
    # sols.printLL(head)
    print('Is loop in LL: ', sols.detectLoop(head))
    print('Is loop in LL: ', sols.detectLoopUsingFloydsAlgo(head))
    
    head =  Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print('Is loop in LL: ', sols.detectLoop(head))
    print('Is loop in LL: ', sols.detectLoopUsingFloydsAlgo(head))
            