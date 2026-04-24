class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cmap = defaultdict(int)
        for i in range(k):
            cmap[s[i]] += 1
        
        res = 0
        l = 0
        count = 0
        for r in range(k, len(s)):
            cmap[s[r]] += 1
            most = max(cmap.values())
            if r - l - most + 1 > k:
                cmap[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)
        
        return res
