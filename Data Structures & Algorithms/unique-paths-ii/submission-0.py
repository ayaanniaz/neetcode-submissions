class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[-1 for _ in range(m)]for _ in range(n)]
        def ways(i, j):
            if i == n-1 and j == m-1 and obstacleGrid[i][j] == 0:
                return 1
            if i >= n or j >= m or obstacleGrid[i][j] == 1:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = ways(i+1, j) + ways(i, j+1)
            return ways(i+1, j) + ways(i, j+1)
        
        return ways(0,0)
            


        