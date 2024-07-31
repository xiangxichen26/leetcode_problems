class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        size = len(quiet)
        indegrees = [0 for _ in range(size)]
        answer = [idx for idx in range(size)]
        # create the graph
        graph = defaultdict(list)
        for rich, poor in richer:
            graph[rich].append(poor)
            indegrees[poor] += 1
        
        queue = deque()
        for i in range(size):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            x = queue.pop() 

            for y in graph[x]:
                if quiet[answer[x]] < quiet[answer[y]]:
                    answer[y] = answer[x]
                indegrees[y] -= 1
                if not indegrees[y]:
                    queue.append(y)
        
        return answer


         