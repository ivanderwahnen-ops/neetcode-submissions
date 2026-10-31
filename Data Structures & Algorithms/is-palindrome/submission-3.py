class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = s.lower().replace(" ", "") 
        l, r = 0, len(clean_s) - 1

        while l < r:

            while l<r and not clean_s[l].isalnum():
                l += 1
            while r>l and not clean_s[r].isalnum():
                r-= 1
            if clean_s[l] != clean_s[r]:
                return False
            l,r = l+1,r-1
        return True
