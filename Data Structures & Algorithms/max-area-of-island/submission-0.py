class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        seen = set()
        ans = 0

        def dfs(i, j):
            nonlocal res

            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return
            if (i, j) in seen:
                return

            seen.add((i, j))
            res += 1

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in seen:
                    res = 0
                    dfs(i, j)
                    ans = max(ans, res)

        return ans