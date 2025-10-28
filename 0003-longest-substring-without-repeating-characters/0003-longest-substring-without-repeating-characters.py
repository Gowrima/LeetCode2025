class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        substr = ''
        cur_len = 0

        while j < len(s):
            if s[j] in substr:
                j = i
                i += 1
                substr = s[j]
            else:
                substr += s[j]
            
            j += 1

            if len(substr) > cur_len:
                cur_len = len(substr)
        
        return cur_len