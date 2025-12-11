from collections import deque

print(deque())  # deque([])
print(deque([1, 3, 5]))    # deque([1, 3, 5])
print(deque('dsa')) # deque(['d', 's', 'a'])
print(deque([2,'ddd']))  # deque([2, 'ddd'])

llist = deque(['a', 'b', 'c', 'd', 'e'])
print(llist)
llist.append('f')
print(llist)
pop_ele = llist.pop()
print(pop_ele)
llist.appendleft('z')
print(llist)
left_pop = llist.popleft()
print(left_pop)
