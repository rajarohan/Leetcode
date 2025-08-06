def allsubseq(a):
    n = len(a)
    ans = []
    def bt(i, ds):
        if i == n:
            ans.append(ds[:])
            return
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
      
