class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        offset = ord('a')
        for s in strs:
            fmap = [0] * 26
            for c in s:
                fmap[ord(c) - offset] += 1
            res[tuple(fmap)].append(s)

        return list(res.values())

        