class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t):
            return False
            
        for i in t:
            if s.count(i) != t.count(i):
                return False
        return True