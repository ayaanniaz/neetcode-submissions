class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        mp = defaultdict(list)
        for i in strs:
            c = [0]*26
            for j in i:
                c[ord(j)-ord('a')] += 1
            mp[''.join(str(c))].append(i)
            
        return list(mp.values())       

                
        