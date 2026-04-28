class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        res = 0

        def dfs(i, j):
            if (i < 0 or j < 0 or 
                i == rows or j == cols or 
                grid[i][j] == '0' or (i,j) in visited):
                return False

            visited.add((i,j))

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

            return True

            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visited:
                    dfs(row,col)
                    res += 1

        return res

