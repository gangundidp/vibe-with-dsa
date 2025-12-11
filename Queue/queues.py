from collections import deque

class Queue:
    def __init__(self, *elements):
        self.queue = deque(elements)
    
    def enqueue(self, ele):
        self.queue.append(ele)
        return len(self.queue)
    
    def dequeue(self):
        popped_item = self.queue.popleft()
        return popped_item
    
    def __len__(self):
        return len(self.queue)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
    
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
len_of_queue = queue.enqueue(3)
print(f"len of queue: {len_of_queue}")

queue.dequeue()

print(f"len of queue: {len(queue)}")

for ele in queue:
    print(ele)
    
print(f"len of queue: {len(queue)}")
