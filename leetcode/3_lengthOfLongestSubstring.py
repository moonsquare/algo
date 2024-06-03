
# 滑动窗口
def lengthOfLongestSubstring(s: str) -> int:
    result = 0
    if s and len(s) > 0:
        s_length = len(s)
        left_start = 0
        t_dic = set()
        for i in range(s_length):
            char = s[i]
            if char in t_dic:
                result = max(result, i - left_start)
                t_dic.remove(s[left_start])
                left_start += 1
                # 连续两个重复字符处理,继续+1
                while left_start < i and char in t_dic:
                    t_dic.remove(s[left_start])
                    left_start += 1
                t_dic.add(char)
            else:
                t_dic.add(char)
        result = max(result, s_length - left_start)
    return result


s = "pwwkew"
print(lengthOfLongestSubstring(s))
