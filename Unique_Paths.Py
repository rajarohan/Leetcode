class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def bt(i, j):
            if i == m or j == n:
                return 0
            if i == (m - 1) and j == (n - 1):
                return 1
            return bt(i + 1, j) + bt(i, j + 1)
        ans = bt(0, 0)
        return ans
