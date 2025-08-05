class Solution:
    def exist(self, a: List[List[str]], t: str) -> bool:
        rows = len(a)
        col = len(a[0])
        path = set()
        def dfs(r, c, i):
            if i == len(t):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= col or t[i] != a[r][c] or (r, c) in path):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)) or 
                (dfs(r - 1, c, i + 1)) or 
                (dfs(r, c + 1, i + 1)) or 
                (dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False
