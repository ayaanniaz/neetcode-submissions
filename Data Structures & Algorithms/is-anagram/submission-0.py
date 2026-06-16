class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        mp1 = defaultdict(int)

        if len(s) != len(t):
            return False
        for i in s:
            mp1[i] += 1
        for i in t:
            mp1[i] -= 1
        for val in mp1.values():
            if val != 0:
                return False
        return True

        


        