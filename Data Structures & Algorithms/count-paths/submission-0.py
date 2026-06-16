class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = [[-1 for i in range(n+1)]for i in range(m+1)]
        def res(i, j):
            if t[i][j] != -1:
                return t[i][j]
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            
            ways1 = res(i+1, j)
            ways2 = res(i, j+1)
            t[i][j] = ways1+ways2
            return t[i][j]
        return res(0,0)

            