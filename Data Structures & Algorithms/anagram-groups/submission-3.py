class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = []
        mp = defaultdict(list)
        for word in strs:
            arr = [0]*26
            for i in word:
                arr[ord(i)-ord('a')] += 1
            mp[''.join(str(arr))].append(word)
        return list(mp.values())





             

                
        