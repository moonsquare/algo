def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    dic = set()
    rk, ans = -1, 0
    for i in range(n):
        if i != 0:
            dic.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in dic:
            dic.add(s[rk + 1])
            rk += 1
        ans = max(ans, rk - i + 1)
    return ans
