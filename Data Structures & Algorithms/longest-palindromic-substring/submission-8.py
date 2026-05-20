class Solution:
    def longestPalindrome(self, s: str) -> str: 
        res = s[0]
        pMap = [[False] * len(s) for _ in range(len(s))]

        for l in range(len(s)):
            r = len(s)-1
            while l < r:
                if pMap[l][r]:
                    break

                if r-l+1 > len(res) and self.is_palindrome(s[l:r+1]):
                    pMap[l][r] = True
                    res = s[l:r+1]
                r -= 1 

        return res
            

    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False 

            l += 1
            r -= 1

        return True
                

                

