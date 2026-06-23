class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr_sum = 0
        for i in nums:
            curr_sum += i
            res = max(res, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return res
        