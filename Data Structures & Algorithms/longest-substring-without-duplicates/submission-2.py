class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in stringSet:
                stringSet.remove(s[l])
                l  += 1
            stringSet.add(s[r])
            res = max(res, r - l + 1)
        return res