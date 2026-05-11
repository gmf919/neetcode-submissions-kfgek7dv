class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        components = 0
        hmap = collections.defaultdict(list)
        visited = set()

        for a,b in edges:
            hmap[a].append(b)
            hmap[b].append(a)

            

        def dfs(node):

            if node in visited:
                return

            visited.add(node)
            for neighbor in hmap[node]:
                dfs(neighbor)
        

        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        return components