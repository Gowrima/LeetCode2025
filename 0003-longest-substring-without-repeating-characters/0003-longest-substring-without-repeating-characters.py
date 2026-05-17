class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i, j = 0, 0
        substr = ''

        while j < len(s):
            if s[j] in substr:
                j = i
                i += 1
                substr = s[j]
            else:
                substr += s[j]    

            if len(substr) > max_len:
                max_len = len(substr)
            
            j += 1

        
        return max_len





