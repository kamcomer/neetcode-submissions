class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0, 1), (0,-1), (1,0),(-1,0)]

        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        pacific_boarder = []
        atlantic_boarder = []

        for c in range(COLS):
            pacific_boarder.append((0,c))
            atlantic_boarder.append((ROWS-1,c))
        
        for r in range(ROWS):
            pacific_boarder.append((r,0))
            atlantic_boarder.append((r,COLS-1))

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr >= 0 and nc >= 0 and
                        nr < ROWS and nc < COLS and
                        not ocean[nr][nc] and
                        heights[r][c] <= heights[nr][nc] 
                    ):
                        q.append((nr,nc))

        bfs(pacific_boarder, pac)
        bfs(atlantic_boarder, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])

        return res

        