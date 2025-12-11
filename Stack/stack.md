**STACK DATA STRUCTURE**
A stack is a data structure that stores items in an Last-In/First-Out manner. This is frequently referred to as LIFO. This is in contrast to a queue, which stores items in a First-In/First-Out (FIFO) manner.

**Implementing a Python Stack**
There are a couple of options when you’re implementing a Python stack.

- list
- collections.deque
- queue.LifoQueue

# Using list to Create a Python Stack
The built-in list structure that you likely use frequently in your programs can be used as a stack. Instead of .push(), you can use .append() to add new elements to the top of your stack, while .pop() removes the elements in the LIFO order.

Unfortunately, list has a few shortcomings. The biggest issue is that it can run into speed issues as it grows. List stores Elements in continuous memory.

If your stack grows bigger than the block of memory that currently holds it, then Python needs to do some memory allocations. This can lead to some .append() calls taking much longer than other ones.

If you use .insert() to add an element to your stack at a position other than the end, it can take much longer. 


# Using collections.deque to Create a Python Stack
The collections module contains deque, which is useful for creating Python stacks. deque is pronounced “deck” and stands for “double-ended queue.”

## Why Have deque and list?
As list built upon continous memory allocation, list methods, like indexing into the list. Getting myList[3] is fast.

The contiguous memory layout is the reason that list might need to take more time to .append() some objects than others. If the block of contiguous memory is full, then it will need to get another block, which can take much longer than a normal .append().

deque, on the other hand, is built upon a doubly linked list. In a linked list structure, each entry is stored in its own memory block and has a reference to the next entry in the list.

Adding a new entry into a linked list structure only requires setting the new entry’s reference to point to the current top of the stack and then pointing the top of the stack to the new entry.  Getting myDeque[3] is slower than it was for a list, because Python needs to walk through each node of the list to get to the third element.

The constant time .append() and .pop() operations make deque an excellent choice for implementing a Python stack if your code doesn’t use threading.

## Python Stacks and Threading
To start with the simpler one, you should never use list for any data structure that can be accessed by multiple threads. list is not thread-safe. Python stacks can be useful in multi-threaded programs .

deque is a little more complex, however. If you read the documentation for deque, it clearly states that both the .append() and .pop() operations are atomic, meaning that they won’t be interrupted by a different thread.So if you restrict yourself to using only .append() and .pop(), then you will be thread safe.

##  LifoQueue is designed to be fully thread-safe.
All of its methods are safe to use in a threaded environment. It also adds optional time-outs to its operations which can frequently be a must-have feature in threaded programs.

This full thread safety comes at a cost, however. To achieve this thread-safety, LifoQueue has to do a little extra work on each operation, meaning that it will take a little longer.

In general, you should use a deque if you’re not using threading. If you are using threading, then you should use a LifoQueue unless you’ve measured your performance and found that a small boost in speed for pushing and popping will make enough difference to warrant the maintenance risks.