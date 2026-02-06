class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        /*
        Approach 1: sort each word
        eat -> sort -> aet
        tea -> sort -> aet
        
        Map<String, List<String>>
        aet: [eat, tea]    
        ..
        
        N = number of words
        M = length of largest word
        Time: N * Mlog(M)
        Space: 2*N
        
        Approach 2: leverage the fact that each string only uses 26 characters (lowercase English letters)
        A: 1
        B: 0
        C: 0
        D: 0
        E: 0
        ...
        N: 1
        T: 1
        ...
        Z: 0
        
        tea
        1|0|0|.....
        
        Map<String, List<String>>
        "1|0|0|.....": [tea]
        
        tan
        
        10^4 * a bucket of size 26
        
        Time: N * M
        */
        
        Map<String, List<String>> map = new HashMap<>();
        
        for (String str : strs) {
            Map<Integer, Integer> charMap = new HashMap<>();
            for (int ii=0; ii<26; ii++) {
                charMap.put(ii, 0);
            }
            
            for (Character ch : str.toCharArray()) {
                int charVal = ch - 'a';
                int charCount = charMap.get(charVal);
                charMap.put(charVal, charCount + 1);
            }
            
            String key = charMap.toString();
            List<String> list = map.getOrDefault(key, new ArrayList<>());
            list.add(str);
            map.put(key, list);
        }
        
        // System.out.println(map);
        List<List<String>> ans = new ArrayList<>();
        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            List<String> list = entry.getValue();
            ans.add(list);
        }
        return ans;
    }
}