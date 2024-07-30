class Solution:
    def topologicalSortKahn(self,numCourses: int, graph:dict) -> bool :
        # calcuate the indegree
        indegrees = {u: 0 for u in graph}
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1
        
        # append all 0 indegree into the queue
        q = deque(u for u in indegrees if indegrees[u] == 0)
        order = []
        while q:
            node = q.pop()
            order.append(node)
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        if len(order) != numCourses:
            return False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build a graph
        graph = dict()
        for i in range(numCourses):
            graph[i] = []
        for u,v in prerequisites:
            graph[v].append(u)

        return self.topologicalSortKahn(numCourses, graph)



        

        