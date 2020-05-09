def lengthOfLongestSubstring(s: str) -> int:
    index = 0
    s1 = ''
    s2 = ''
    while s:
        s1 = s[index]
        s = s[index + 1: len(s)]
        for sub in s:
            if sub in s1:
                # we need to break out because we done checking
                break
            else:
                s1 += sub
        if len(s1) > len(s2):
            s2 = s1
    return len(s2)