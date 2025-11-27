from collections import defaultdict

class Solution:
    def dfs(self, graph, s, d):
        marked = set()
        visited = [s]
     
        while visited:
            v = visited.pop()

            if v not in marked:
                marked.add(v)
            
                for nei in graph[v]:
                    if nei == d:
                        return True    

                    if nei not in marked:
                        visited.append(nei)
            
        return False


    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges and source == destination:
            return True

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return self.dfs(graph, source, destination)