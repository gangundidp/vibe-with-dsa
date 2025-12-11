# Heap
 A tree-based data structure in which the value of a parent node is ordered in a certain way with respect to the value of its child node(s). 
 
 A heap can be either a min heap (the value of a parent node is less than or equal to the value of its children) or a max heap (the value of a parent node is greater than or equal to the value of its children).

 The purpose of a min-heap is to store objects that have a partial order on them. It has a fast (O(log n)) method for removing the minimum object from the heap. Min-heaps are useful for calculations where you have multiple minimum computations to perform.

There is an analogous structure called a max-heap, which extracts the maximum value from the heap. A heap is either a max-heap or a min-heap - it can't be both. A max-heap can be implemented by reversing the comparison between elements. 

Heaps are sometimes referred to as priority queues. Technically, heaps are actually just one implementation of a priority queue.

### Crucial Terms

**key**: The values that determine the order. If you're storing numbers, the numbers can be the keys. If you're storing more complicated objects, the key is the data field that we're comparing by. Unlike in hash tables, keys in heaps do not have to be unique.

**extract_min**: The method of (quickly) being able to extract the minimum element from the min-heap.


### Strengths
A min-heap is able to quickly extract the minimum value on the heap. Repeated extractions from a min-heap into an array will yield a sorted array.

### Weaknesses
There's no convenient way of searching for a particular key value in a heap. Entries are only partially ordered; clever use of the heap property can allow for some pruning of searches.


## In Interviews, Use Heaps When ...

Heaps are designed to do one specific thing well, so the answer to when you should use a heap is repetitive: You use one when you have to do repeated minimum (or maximum) extractions. The problems where you would want to do this might look quite different from each other, however. Below we have selected some examples of common interview questions that benefit from heaps.

*Finding the minimum distance between two nodes in a graph:*
The standard approach to this problem is to use Dijkstra's algorithm. One of the key steps in Dijkstra's algorithm is to select the node closest to a node that you have already completed, which is a minimum calculation.

*Getting the next event that is scheduled to occur:*
Storing events in a heap with a timestamp as the key gives you a fast way to extract the next event (the event with the smallest timestamp will occur next).

*Keep track of the median value while streaming:*
This is the running median problem, where two heaps are maintained: a max-heap for values below the current median and a min-heap for values above the current median. When a new value is inserted, it is placed in the low or high pile as appropriate (and the maximum of the low values or minimum of the low values are extracted as necessary to keep the two heaps sizes' different by at most one element).

Find the *first k non-repeating characters* in a string in a single traversal.


### MinHeap operations
1. Insertion O(logn): Finding the exact position of the new element is performed in logn since it is only compared with the position of the parent nodes.

2. Delete Min O(logn): After the minimum element is removed, the heap has to put the new root in place.

3. Find Min O(1): This is possible because the heap data structure always has the minimum element on the root node.

4. Heapify O(n): This operation rearranges all the nodes after deletion or insertion operation. The cost of this operation is n since all the elements have to be moved to keep the heap properties.

5. Delete O(logn): A specific element from the heap can be removed in logn time.