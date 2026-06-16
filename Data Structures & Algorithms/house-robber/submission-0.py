class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1 for _ in range(len(nums)+1)]
        def res(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(nums[i] + res(i+2), res(i+1))
            return dp[i]
        
        return max(res(0), res(1))