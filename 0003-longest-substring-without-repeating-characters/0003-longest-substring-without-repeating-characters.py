class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        max_len = 0
        i, j = 0, 0
        
        if not s:
            return 0
        
        while j < len(s):
            if s[j] in substr:
                j = i
                i += 1
                substr = s[j]     
            else:
                substr += s[j]
            
            j += 1
            
            if len(substr) > max_len:
                max_len = len(substr)
        
        return max_len
