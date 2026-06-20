class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        from typing import List
        adj = defaultdict(list)
        indegree = [0]*(numCourses)

        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        q = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        topo = []

        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(topo) != numCourses:
            return []
        return topo
        