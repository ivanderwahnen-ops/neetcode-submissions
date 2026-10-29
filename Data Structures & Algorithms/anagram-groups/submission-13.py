class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen_dicts = defaultdict(list)
        
        for s in strs:
            dict_s = {}
            for i in s:
                dict_s[i] = 1 + dict_s.get(i, 0)
            seen_dicts[frozenset(dict_s.items())].append(s)

        return list(seen_dicts.values())