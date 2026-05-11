class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(x,y,visited,previousHeight):

            if 0 <=  x < rows and 0 <= y < cols and (x,y) not in visited and heights[x][y] >= previousHeight:

                visited.add((x,y))

                dfs(x + 1,y,visited,heights[x][y])
                dfs(x - 1,y,visited,heights[x][y])
                dfs(x,y + 1,visited,heights[x][y])
                dfs(x,y - 1,visited,heights[x][y])

        
        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols-1])

        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1,col, atlantic, heights[rows-1][col])

        res = []

        for x in range(rows):
            for y in range(cols):
                if (x,y) in pacific and (x,y) in atlantic:
                    res.append([x,y])

        return res
            



            