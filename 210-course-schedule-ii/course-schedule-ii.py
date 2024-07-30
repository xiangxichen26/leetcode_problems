class Solution:
    def topologicalSortKahn(self, numCourses: int, graph: dict) -> List[int]:
        indegrees= {u:0 for u in graph}
        for node in graph:
            for nei in graph[node]:
                indegrees[nei] += 1
        
        q = deque()
        for node in graph:
            if indegrees[node] == 0:
                q.append(node)
        
        order = []
        while q:
            node = q.pop()
            order.append(node)
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        if len(order) != numCourses:
            return []
        return order

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the graph
        graph = dict()
        for i in range(numCourses):
            graph[i] = []
        for u,v in prerequisites:
            graph[v].append(u)
        
        return self.topologicalSortKahn(numCourses,graph)