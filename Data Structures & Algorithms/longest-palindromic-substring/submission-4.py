class Solution:
    def longestPalindrome(self, s: str) -> str: 
        res = ""

        for l in range(len(s)):
            r = len(s)-1
            while l < r:
                if r-l+1 > len(res) and self.is_palindrome(s[l:r+1]):
                    res = s[l:r+1]

                r -= 1 

        if not res:
            res = s[0]

        return res
            

    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False 

            l += 1
            r -= 1

        return True
                

                

