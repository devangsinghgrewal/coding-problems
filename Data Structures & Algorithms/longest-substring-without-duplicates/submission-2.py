class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_length = 0, 0
        d = {}

        for r, ch in enumerate(s):
            if ch in d:
                l = max(l, d[ch] + 1)
            d[ch] = r
            max_length = max(max_length, r - l + 1)
        return max_length