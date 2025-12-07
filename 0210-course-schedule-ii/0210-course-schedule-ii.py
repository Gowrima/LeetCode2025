from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topo_sort = []
        visited = list()
        graph = defaultdict(list)
        in_degree = [0] * numCourses

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

        if len(topo_sort) == numCourses:
            return topo_sort
        else:
            return []
        