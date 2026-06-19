class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pac, alt = set(), set()

        def dfs(i, j, seen, prevHeight):
            if i < 0 or j < 0 or i >= n or j >= m or (i,j) in seen or heights[i][j] < prevHeight:
                return 
            
            seen.add((i, j))
            dfs(i+1, j, seen, heights[i][j])
            dfs(i-1, j, seen, heights[i][j])
            dfs(i, j+1, seen, heights[i][j])
            dfs(i, j-1, seen, heights[i][j])

        for r in range(n):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, m-1, alt, heights[r][m-1])
        
        for c in range(m):
            dfs(0, c, pac, heights[0][c])
            dfs(n-1, c, alt, heights[n-1][c])
        
        res = []
        for i in range(n):
            for j in range(m):
                if (i,j) in pac and (i,j) in alt:
                    res.append([i,j])
        return res
        