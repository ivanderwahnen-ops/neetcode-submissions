class Solution:

    def encode(self, strs: List[str]) -> str:
        to_encode = []

        for s in strs:
            to_encode.append(str(len(s)) + '#'+ s)
        return ''.join(to_encode)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = 1 + j
            j = i + length
            res.append(s[i:j])
            i = j

        return res
