from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        dict = key = char, val = # occurances

        a:1, b:1, c:1

        for every char in s, get the substring, cba --> # of occurances in p len(p)

        dict = time O(p), space O(p)

        time = O(s) + to check in the dict = O(substr of len p) = O(s+substr of len p)
            = O(s)

        total time = O(p+s), space = O(p)

        s="abc"
        p="abcdefg"

        build dict from string p with key = char and value = frequency

        for every char c in s, look up c+len(p) in the dict = add it to the output array

        s = "cbaebabacd", p = "abc"

        s = "abaqwer", p = "abc"
             | |
              i j
        """
        p_len, s_len = len(p), len(s)
        result = []

        if p_len > s_len:
            return result

        p_dict = defaultdict(int)
        s_dict = defaultdict(int)

        for c in p:
            p_dict[c] += 1

        for i in range(0, p_len):
            s_dict[s[i]] += 1

        if p_dict == s_dict:
            result.append(0)

        # s = "abab", p = "ab"
        i, j = 1, p_len

        while j < s_len:
            if s_dict[s[i - 1]] > 1:
                s_dict[s[i - 1]] -= 1
            else:
                del s_dict[s[i - 1]]

            s_dict[s[j]] += 1

            if p_dict == s_dict:
                result.append(i)

            i += 1
            j += 1

        return result

        # s=ABAB
        # p=AB

        # dict_1 = s[i:j] = aba
        # dict_2 = s[i : j + 1] = baq
        #
        # dict_1 = s[1:3]
        # dict_2 = s[1:3]
        # dict_3 = s[2:4]
