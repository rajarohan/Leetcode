def allsubseq(a):
    n = len(a)
    ans = []
    def bt(i, ds):
        if i == n:
            ans.append(ds[:])
            return
        if i != (n - 1) and a[i] < a[i + 1]:
            ds.append(a[i])
            bt(i + 1, ds)
            ds.pop()
        bt(i + 1, ds)
    bt(0, [])
    return ans
def is_increasing(a):
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            return False
    return True

def longest_Subsequence(a):
    all = allsubseq(a)
    maxi = 0
    for i in all:
        if is_increasing(i):
            maxi = max(maxi, len(i))
    return maxi
#Memoization
def longest_Subsequence(a):
    n = len(a)
    def dp(i, prev):
        if i == n:
            return 0
        
        notT = dp(i + 1, prev)
        
        T = 0
        if prev == -1 or a[i] > a[prev]:
            T = 1 + dp(i + 1, i)
        
        return max(T, notT)

    return dp(0, -1)
print(longest_Subsequence([1, 3, 2, 4, 0, 9]))
