class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        map_1 = {}
        map_2 = {}

        for i in range(len(s)):
            map_1[s[i]] = map_1.get(s[i], 0) + 1
            map_2[t[i]] = map_2.get(t[i], 0) + 1
        
        if map_1 == map_2:
            return True
        else:
            return False
            
        