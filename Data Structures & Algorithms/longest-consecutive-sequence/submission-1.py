class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in numSet:
            if i-1 not in numSet:
                l = 1
                while i+l in numSet:
                    l += 1
                res = max(res, l)
        return res
                
                
        