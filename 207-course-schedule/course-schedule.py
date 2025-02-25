class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        # bi->ai
        graph = collections.defaultdict(list)
        for i, j in prerequisites:
            graph[j].append(i)
        
        arrive = set()
        leave = set()

        # dfs
        def dfs(node):
            arrive.add(node)

            for nei in graph[node]:
                if nei not in arrive:
                    if not dfs(nei):
                        return False
                elif nei not in leave:
                    return False
            
            leave.add(node)
            return True
        
        for i in range(numCourses):
            if i not in arrive:
                if not dfs(i):
                    return False
        return True