class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        offset = ord('a')
        fmap = [0] * 26
        for c in s:
            fmap[ord(c) - offset] += 1

        for c in t:
            fmap[ord(c) - offset] -= 1

        for i in fmap:
            if i != 0:
                return False

        return True
        
        