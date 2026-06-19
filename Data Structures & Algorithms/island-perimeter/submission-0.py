class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = set()
        def dfs(i,j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 1
            if (i,j) in seen:
                return 0
            seen.add((i,j))
            res = dfs(i, j+1) + dfs(i+1, j) + dfs(i-1 ,j) + dfs(i, j-1)
            return res
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0
    
            
            

        