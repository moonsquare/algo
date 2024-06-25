class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        max_len = max(l1, l2)
        carry = 0
        ans = ""
        for i in range(max_len):
            n1 = 0
            n2 = 0
            if i < l1:
                n1 = int(num1[l1 - i - 1])
            if i < l2:
                n2 = int(num2[l2 - i - 1])
            t_sum = n1 + n2 + carry
            ans = str(t_sum % 10) + ans
            carry = t_sum // 10
        if carry > 0:
            ans = str(carry) + ans
        return ans
so = Solution()
so.addStrings("11","123")