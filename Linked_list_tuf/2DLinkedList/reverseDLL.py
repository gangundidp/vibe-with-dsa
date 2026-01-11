class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
class Solution:
    def reverseDll(self, head):
        if (head == None or head.next == None):
            return head
        
        temp = head
        stack = []
        
        while temp:
            stack.append(temp.data)
            temp = temp.next
        
        temp = head
        while temp:
            temp.data = stack.pop()
            temp = temp.next
            
        return head
    
    def reverseDllOptimal(self, head):
        if (head == None or head.next == None):
            return head
        
        temp = head
        while temp.next is not None:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev
        temp.next, temp.prev = temp.prev, temp.next
        # self.printDll(temp)
            
        return temp
        
    def printDll(self, head):
        print(None, end='<->')
        while head:
            print(head.data, end='<->')
            head = head.next
        print(None)
        
if __name__ == "__main__":
    sols = Solution()
    
    head = Node(1)
    head.next = Node(2, head)
    head.next.next = Node(3, head.next)
    head.next.next.next = Node(4, head.next.next)

    sols.printDll(head)
    head = sols.reverseDll(head)
    sols.printDll(head)
    
    head = Node(1)
    head.next = Node(2, head)
    head.next.next = Node(3, head.next)
    head.next.next.next = Node(4, head.next.next)
    sols.printDll(head)
    head = sols.reverseDllOptimal(head)
    sols.printDll(head)