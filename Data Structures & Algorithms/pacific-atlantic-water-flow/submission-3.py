class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Define grid
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            # Determin if cell is already visited or is out of bounds
            if ((r, c) in visited or 
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                heights[r][c] < prev_height
            ):
                return

            # Add current cell to visited
            visited.add((r,c))

            # Explore grid
            curr_height = heights[r][c]
            dfs(r-1,c,visited, curr_height)
            dfs(r+1,c,visited, curr_height)
            dfs(r,c-1,visited, curr_height)
            dfs(r,c+1,visited, curr_height)

            return

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
