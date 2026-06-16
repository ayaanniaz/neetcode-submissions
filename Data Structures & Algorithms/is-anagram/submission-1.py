class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        m1 = defaultdict(int)
        m2 = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            m1[s[i]] += 1
            m2[t[i]] += 1
        
        for i in range(len(s)):
            if m1[s[i]] != m2[s[i]]:
                return False
        return True
        

        

        


        