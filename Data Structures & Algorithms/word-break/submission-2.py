class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s): True}

        def dfs(i):
            if i in cache:
                return cache[i]
            
            for word in wordDict:
                if ((i+len(word)) <= len(s) and s[i:i+len(word)] == word): 
                    if dfs(i+len(word)):
                        cache[i] = True
                        return True
            cache[i] = False
            return False

        return dfs(0)