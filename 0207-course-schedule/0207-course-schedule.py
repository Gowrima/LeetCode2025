from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        visited = list()
        topo_sort = list()

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])        
            in_degree[prereq[0]] += 1
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                visited.append(i)
        
        while visited:
            v = visited.pop()
            topo_sort.append(v)

            for nei in graph[v]:
                in_degree[nei] -= 1

                if in_degree[nei] == 0:
                    visited.append(nei)
        
        return len(topo_sort) == numCourses