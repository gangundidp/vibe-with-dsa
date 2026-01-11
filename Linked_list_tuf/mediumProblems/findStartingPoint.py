class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Solution:
    def findStartingPointOfLoop(self, head):
        visited = set()
        
        while head:
            if head in visited:
                return head.data
            visited.add(head)
            head = head.next
        return None
    
    def tortoiseAndHareAlgo(self, head):
        fast = slow = head
        
        while (fast is not None) and (fast.next is not None):
            fast = fast.next.next
            slow = fast.next
            if fast == slow:
                slow = head
                while fast != slow:
                    print('tere')
                    fast = fast.next
                    slow = slow.next
            return fast.data
        return None
    
if __name__ == "__main__":
    sols = Solution()
    
    head = Node(1)
    head.next = Node(2, Node(3))
    head.next.next.next = Node(4, Node(5, head.next.next))
    
    # sols.printLL(head)
    print('Starting Point: ', sols.findStartingPointOfLoop(head))
    print('Starting Point: ', sols.tortoiseAndHareAlgo(head))
    
    head =  Node(1, Node(2, Node(3, Node(4, Node(5, Node(3))))))
    print('Starting Point: ', sols.findStartingPointOfLoop(head))
    print('Starting Point: ', sols.tortoiseAndHareAlgo(head))
            
        