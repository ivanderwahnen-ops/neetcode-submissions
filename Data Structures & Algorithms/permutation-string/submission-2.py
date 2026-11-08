class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        char_frq_s1 = {}
        char_frq_s2wnd = {}

        for i in range(len(s1)):
            char_frq_s1[s1[i]] = 1 + char_frq_s1.get(s1[i], 0)
            char_frq_s2wnd[s2[i]] = 1 + char_frq_s2wnd.get(s2[i], 0)

        if char_frq_s1 == char_frq_s2wnd: return True

        for r in range(len(s1), len(s2)):
            entering = s2[r]
            leaving = s2[r - len(s1)]

            char_frq_s2wnd[entering] = char_frq_s2wnd.get(entering, 0) + 1
            char_frq_s2wnd[leaving] -= 1

            if char_frq_s2wnd[leaving] == 0:
                del char_frq_s2wnd[leaving]

            if char_frq_s1 == char_frq_s2wnd:
                return True
        return False

        