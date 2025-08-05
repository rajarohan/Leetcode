class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.ref = -1

    def insert(self, w, ref):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.ref = ref

class Solution:
    def findWords(self, mat: List[List[str]], a: List[str]) -> List[str]:
        def dfs(node, i, j):
            ind = ord(mat[i][j]) - ord('a')
            if node.children[ind] is None:
                return
            node = node.children[ind]
            if node.ref >= 0:
                ans.append(a[node.ref])
                node.ref = -1
            c = mat[i][j]
            mat[i][j] = 0
            for aa, b in pairwise((0, 1, 0, -1, 0)):
                x = i + aa
                y = j + b
                if 0 <= x < m and 0 <= y < n and mat[x][y] != 0:
                    dfs(node, x, y)
            mat[i][j] = c
        tree = Trie()
        for i, w in enumerate(a):
            tree.insert(w, i)
        m = len(mat)
        n = len(mat[0])
        ans = []
        for i in range(m):
            for j in range(n):
                dfs(tree, i, j)
        return ans
