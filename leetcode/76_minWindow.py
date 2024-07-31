import sys
from collections import Counter


class Solution:
    def minWindow_1(self, s: str, t: str) -> str:
        ans = ""
        t_dict = Counter(t)
        s_simple = []
        for i, val in enumerate(s):
            if val in t_dict:
                s_simple.append([i, val])
        if not s_simple:
            return ans
        sub_dict = {}
        min_len = sys.maxsize
        t_dict_check = t_dict.copy()
        j = 0
        less_char = s_simple[j][1]
        for [i, end] in s_simple:
            # 记录每个元素有多少个
            if end in sub_dict:
                sub_dict[end] += 1
            else:
                sub_dict[end] = 1
            # 去除已满足的元素
            if end in t_dict:
                if t_dict[end] == 1:
                    t_dict.pop(end)
                else:
                    t_dict[end] -= 1
            # 已满足
            if not t_dict:
                while sub_dict[less_char] >= t_dict_check[less_char]:
                    start_i = s_simple[j][0]
                    if i - start_i < min_len:
                        min_len = i - start_i
                        ans = s[start_i:i + 1]
                    less_char = s_simple[j][1]
                    sub_dict[less_char] -= 1
                    j += 1
        return ans

    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, len(s)
        left = 0
        cnt_s = Counter()  # s 子串字母的出现次数
        cnt_t = Counter(t)  # t 中字母的出现次数
        less = len(cnt_t)  # 有 less 种字母的出现次数 < t 中的字母出现次数
        for right, c in enumerate(s):  # 移动子串右端点
            cnt_s[c] += 1  # 右端点字母移入子串
            if cnt_s[c] == cnt_t[c]:
                less -= 1  # c 的出现次数从 < 变成 >=
            while less == 0:  # 涵盖：所有字母的出现次数都是 >=
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                x = s[left]  # 左端点字母
                if cnt_s[x] == cnt_t[x]:
                    less += 1  # x 的出现次数从 >= 变成 <（下一行代码执行后）
                cnt_s[x] -= 1  # 左端点字母移出子串
                left += 1  # 移动子串左端点
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]


so = Solution()

print(so.minWindow("ADOBECODEBANC", "ABC"))
