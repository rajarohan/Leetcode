#for task can't solve
class Solution:
    def eraseOverlapIntervals(self, a: List[List[int]]) -> int:
        n = len(a)
        a.sort(key = lambda x : x[1])
        p = float('-inf')
        for i, j  in a:
            if p <= i:
                n -= 1
                p = j
        return n

#for task can solve
class Solution:
    def eraseOverlapIntervals(self, a: List[List[int]]) -> int:
        n = 0
        a.sort(key = lambda x : x[1])
        p = float('-inf')
        for i, j  in a:
            if p <= i:
                n += 1
                p = j
        return n



