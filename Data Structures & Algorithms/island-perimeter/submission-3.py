class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        dir4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # res = 0
        seen = set()

        def dfs (r, c):
            if (r, c) in seen: return 0
            if r < 0 or r >= ROWS or c < 0 or c >= COLS: return 1
            if grid[r][c] == 0: return 1
            res = 0
            seen.add((r, c))
            for dr, dc in dir4:
                res += dfs(r+dr, c+dc)
            return res




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)

        # return res