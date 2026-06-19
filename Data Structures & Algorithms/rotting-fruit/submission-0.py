class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        t = 0
        res = 0

        while any(1 in row for row in grid):
            new_rotten = []
            flag = False

            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 2:
                        if j + 1 < m and grid[i][j + 1] == 1:
                            new_rotten.append((i, j + 1))
                        if j - 1 >= 0 and grid[i][j - 1] == 1:
                            new_rotten.append((i, j - 1))
                        if i + 1 < n and grid[i + 1][j] == 1:
                            new_rotten.append((i + 1, j))
                        if i - 1 >= 0 and grid[i - 1][j] == 1:
                            new_rotten.append((i - 1, j))

            for i, j in new_rotten:
                grid[i][j] = 2
                flag = True

            if not flag:
                break

            res += 1
            t += 1

        if any(1 in row for row in grid):
            return -1
        return res
                    


                         


        

        