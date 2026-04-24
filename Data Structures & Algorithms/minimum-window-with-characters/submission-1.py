class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = defaultdict(int)
        for c in t:
            target[c] += 1
        
        res = None
        l = 0
        sub = defaultdict(int)
        for r in range(len(s)):
            sub[s[r]] += 1

            flag = True
            while flag:
                for k, v in target.items():
                    if sub[k] < v:
                        flag = False
            
                if flag:
                    sub_str = s[l:r+1]
                    
                    if not res:
                        res = sub_str
                    else:
                        res = sub_str if len(sub_str) < len(res) else res

                    sub[s[l]] -= 1
                    l += 1
        
        if res is None:
            return ""

        return res

        
        