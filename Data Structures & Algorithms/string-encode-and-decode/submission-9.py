class Solution:

    def encode(self, strs: List[str]) -> str:
        to_encode = []

        for s in strs:
            to_encode.append(str(len(s)) + '#'+ s)
        return ''.join(to_encode)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = s.find("#")
        
        while i < j:
            length = int(s[i:j])
            i = 1 + j
            res.append(s[i:i + length])
            i += length
            j = s.find("#", i)
        return res
