class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def ways(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = ways(i+1, total + nums[i]) + ways(i+1, total - nums[i])
            return ways(i+1, total + nums[i]) + ways(i+1, total - nums[i])
        return ways(0,0)
        