class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def solve(houses):
            dp = [-1]*len(houses)
            def res(i):
                if i >= len(houses):
                    return 0
                if dp[i] != -1:
                    return dp[i]

                dp[i] = max(houses[i] + res(i+2), res(i+1))
                return dp[i]
            return res(0)
        
        res1 = solve(nums[1:])
        res2 = solve(nums[:-1])
        return max(res1, res2)
        