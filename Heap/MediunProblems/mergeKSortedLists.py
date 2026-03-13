import heapq

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        min_heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next

if __name__ == "__main__":
    sol = Solution()

    # Creating three linked lists:
    # list1: 1 -> 4 -> 5
    # list2: 1 -> 3 -> 4
    # list3: 2 -> 6

    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    lists = [list1, list2, list3]
    result = sol.mergeKLists(lists)

    # Print the merged list
    while result:
        print(result.val, end=" ")
        result = result.next
