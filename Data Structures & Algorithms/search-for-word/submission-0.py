class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()
        
        def dfs(r,c,s):
            if (r < 0 or c < 0 or 
                r == rows or c == cols or 
                len(s) > len(word) or
                (r,c) in visit):
                return 
    
            visit.add((r,c))
            s += board[r][c]
    
            res = (s == word or dfs(r-1,c,s) or
                dfs(r+1,c,s) or
                dfs(r,c-1,s) or
                dfs(r,c+1,s))
    
            visit.remove((r,c))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,""):
                    return True

        return False