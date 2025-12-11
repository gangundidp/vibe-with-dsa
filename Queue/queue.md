# Queues
A queue is an abstract data type that represents a sequence of elements arranged according to a set of rules. 

 At the very least, every queue provides operations for adding and removing elements in constant time or O(1) using the Big O notation. That means both operations should be instantaneous regardless of the queue’s size.

**Principle & Operatins**
FIFO is short for first-in, first-out, which describes the flow of elements through the queue. Elements in such a queue will be processed on a first-come, first-served basis, which is how most real-life queues work.

A new element is only allowed to join the queue on one end called the tail—which is on the right, while the oldest element must leave the queue from the opposite end. When an element leaves the queue, then all of its followers shift by exactly one position towards the head of the queue.

Adding an element to the FIFO queue is commonly referred to as an enqueue operation, while retrieving one from it is known as a dequeue operation. Enqueuing and dequeuing are two independent operations that may be taking place at different speeds

*Usecases:*
This fact makes FIFO queues the perfect tool for buffering data in streaming scenarios and for scheduling tasks that need to wait until some shared resource becomes available. For example, a web server flooded with HTTP requests might place them in a queue instead of immediately rejecting them with an error.

# Deque: Double-Ended Queue
A double-ended queue or deque (pronounced deck) is a more generic data type that combines and extends the ideas behind the stack and the queue. It allows you to enqueue or dequeue elements from both ends in constant time at any given moment. Therefore, a deque can work as a FIFO or a LIFO queue, as well as anything in between and beyond.

*Why not use a Python list instead of collections.deque as a building block for your FIFO queue?*
dequeuing an element from the front of a list with list.pop(0), or equivalently inserting one with list.insert(0, element), is far less efficient. Such operations always shift the remaining elements, resulting in a linear, or O(n), time complexity. In contrast, deque.popleft() and deque.appendleft() avoid that step altogether.