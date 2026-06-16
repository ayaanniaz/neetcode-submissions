class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        m1 = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            m1[s[i]] += 1
            m1[t[i]] -= 1
        
        for k, v in m1.items():
            if v != 0:
                return False
        return True 
        
        
        

        

        


        