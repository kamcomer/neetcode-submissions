class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        ROWS, COLS = len(board), len(board[0])
        def dfs(row, col, index, seen):
          if index >= n:
            return True
          if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] != word[index] or (row, col) in seen:
            return False
          seen.add((row, col))
          nei = [[0, 1], [0, -1], [1, 0], [-1, 0]]
          for dx, dy in nei:
            if dfs(row + dx, col + dy, index + 1, seen):
              return True
          seen.remove((row, col))
        for r in range(ROWS):
          for c in range(COLS):
            if dfs(r, c, 0, set()):
              return True
        return False
          