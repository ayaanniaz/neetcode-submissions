class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        m = len(grid[0])

        q  = deque()
        fresh = 0
        time = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while fresh > 0 and q:
            l = len(q)
            for i in range(l):
                r,c = q.popleft()

                for dr, dc in [(1,0), (0,1), (-1,0), (0, -1)]:
                    nr, nc = r+dr, c+dc
                    if nr in range(n) and nc in range(m) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

            
            
        
                    


                         


        

        