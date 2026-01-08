class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    
    # Create first Node
    y = Node(arr[0])
    z = Node(arr[1], y)

    # Print first node address (memory refernce)
    print(y)

    # Print data stored in first node
    print(y.data)
    print(z.next.data)