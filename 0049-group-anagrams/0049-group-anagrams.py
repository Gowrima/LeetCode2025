from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagram = defaultdict(list)

        for s in strs:
            s_sorted = "".join(sorted(s))

            if s_sorted in anagram:
                anagram[s_sorted].append(s)
            else:
                anagram[s_sorted] = [s]
        
        for i in anagram:
            res.append(anagram[i])

        return res