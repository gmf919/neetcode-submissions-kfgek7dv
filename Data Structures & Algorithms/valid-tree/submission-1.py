class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False


        graph = collections.defaultdict(list)


        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(i):

            if i in visited:
                return
            
            visited.add(i)

            for node in graph[i]:

                dfs(node)

        dfs(0)

        return len(visited) == n