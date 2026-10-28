class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        
        dict_s = {}
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        
        for i in t:
            if dict_s.get(i) != t.count(i):
                return False
        return True