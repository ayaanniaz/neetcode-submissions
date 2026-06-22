class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1 for _ in range(m)]for _ in range(n)]

        def res(i, j):
            if i == n-1 and j == m-1:
                return grid[i][j]
            
            if i >= n or j >= m:
                return float('inf')

            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = grid[i][j] + min(res(i+1, j), res(i, j+1))
            return dp[i][j]
        return res(0,0)
            

            
        