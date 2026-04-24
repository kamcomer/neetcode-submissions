class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cmap = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            if c in cmap:
                l = max(cmap[c] + 1, l)
            
            cmap[c] = r
            res = max(r - l + 1, res)

        return res
        
