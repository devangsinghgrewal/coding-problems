from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        da = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in da:
                da[key].append(s)
            else:
                da[key] = [s]
        print(da)
        return list(da.values())