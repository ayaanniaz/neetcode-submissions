class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]

        def ways(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            dp[i] = ways(i-1) + ways(i-2)
            return ways(i-1) + ways(i-2)
        return ways(n)
        