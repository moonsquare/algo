from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        d = {'(': ')', '[': ']', '{': '}'}
        for v in s:
            if v == '(' or v == '[' or v == '{':
                q.append(v)
            elif not q or d.get(q.pop()) != v:
                return False
        if q:
            return False
        return True
