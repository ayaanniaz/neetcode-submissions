class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for _ in range(len(cost)+1)]
        def res(i):
            if i >= len(cost):
                return 0
            
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(res(i+1), res(i+2))

            return dp[i]
        return min(res(0), res(1))




            
            

        