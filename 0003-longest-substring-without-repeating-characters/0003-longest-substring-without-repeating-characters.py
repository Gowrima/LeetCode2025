class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        substr = ''
        maxLen = 0

        while end<len(s):
            if s[end] not in substr:
                substr += s[end]
                maxLen = max(maxLen, len(substr))
            else:
                end = start
                start += 1
                substr = s[end]     

            end += 1

        return maxLen
        