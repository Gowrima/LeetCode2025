class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = ''

        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            else:
                break

        return result