class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = []
        for i in range(len(strs[0])):
            if strs[0][i] == strs[len(strs)-1][i]:
                res.append(strs[0][i])
            else:
                return ''.join(res)
        return ''.join(res)