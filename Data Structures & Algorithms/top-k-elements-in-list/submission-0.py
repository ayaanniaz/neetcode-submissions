class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        c = Counter(nums)
        heap = []
        for key,val in c.items():
            heapq.heappush(heap, (val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [key for val,key in heap]
        