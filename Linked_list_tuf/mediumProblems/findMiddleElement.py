class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    
class Solution:
    def findMiddle(self, head):
        temp = head
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
            
        temp = head
        i = 0
        while i < (count//2):
            temp = temp.next
            i += 1
            
        return temp.data
    
    def tortoiseHareAlgo(self, head):
        slow = fast = head
        
        while (fast is not None) and (fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            
        return slow.data

    def printLL(self, head):
        while head:
            print(head.data, end='->')
            head = head.next
        print(None)
        
if __name__ == "__main__":
    sols = Solution()
    
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    
    sols.printLL(head)
    print("Middle Ele: ", sols.findMiddle(head))
    print("Middle Ele: ", sols.tortoiseHareAlgo(head))
    sols.printLL(head)
    
    print('----------------------------------------')
            
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    
    sols.printLL(head)
    print("Middle Ele: ", sols.findMiddle(head))
    print("Middle Ele: ", sols.tortoiseHareAlgo(head))
    sols.printLL(head)
            
        