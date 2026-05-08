class Solution:
    def canFinish(self,n, prerequisites):
        graph = [[] for _ in range(n)]
        cycle = [False] * n
        for pair in prerequisites:
            graph[pair[0]].append(pair[1])

        def dfs(course):
            if cycle[course]:
                return False
            if graph[course] is None:
                return True
            cycle[course] = True
            for prereq in graph[course]:
                if dfs(prereq) is False:
                    return False
            cycle[course] = False
            graph[course] = []
            return True

        for i in range(n):
            if dfs(i) is False:
                return False
        return True