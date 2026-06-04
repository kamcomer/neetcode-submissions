class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for l in range(len(s)):
            r = l
            for r in range(l, len(s)):
                if self.is_palandrom(s[l:r+1]):
                    res += 1
        return res

    def is_palandrom(self, s: str) -> bool:
        start, end = 0, len(s)-1
        for i in range(len(s)//2):
            if s[start+i] != s[end-i]:
                return False
        return True