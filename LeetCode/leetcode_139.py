# coding=utf-8
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 word_dict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 说明:
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例:
# 输入: s = "leetcode", word_dict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"


def word_break(s, word_dict):
    """
    :type s: str
    :type word_dict: List[str]
    :rtype: bool
    """
    # if len(s) == 0 or not word_dict:
    #     return False
    word_dict = set(word_dict)
    res = [True] + [False for _ in range(len(s))]
    sl = len(s)
    for i in range(sl):
        for j in range(i + 1, sl + 1):
            if res[i] and s[i: j] in word_dict:
                if j == sl:
                    return True
                res[j] = True
    return False


if __name__ == '__main__':
    print word_break('catdogod', ['cat', 'dog', 'god'])
    print word_break('catdogod', ['cat', 'dog', 'od'])
