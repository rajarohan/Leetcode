def find_parent(i, a):
    if i == 0:
        return 
    print(a[(i - 1) // 2])
def find_left_child(i, a):
    idx = 2 * i + 1
    if idx >= len(a):
        return 
    print(a[idx])
def find_right_child(i, a):
    idx = 2 * i + 2
    if idx >= len(a):
        return 
    print(a[idx])

import heapq

a = [10, 20, 15, 30, 40, 5, 8]

heapq.heapify(a)

print(a)
find_right_child(2, a)
