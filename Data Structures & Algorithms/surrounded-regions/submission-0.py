class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        seen = set()
        rows , cols = len(board), len(board[0])
        isBorder = True

        def dfs(x,y,isBorder):
            if (x,y) not in seen and 0 <= x < rows and 0<= y < cols and board[x][y] == 'O':

                if not isBorder:
                    board[x][y] = 'X'

                seen.add((x,y))
                dfs(x + 1,y,isBorder)
                dfs(x - 1,y,isBorder)
                dfs(x,y + 1,isBorder)
                dfs(x,y -1,isBorder)


        for col in range(cols):
            if board[0][col] == 'O':
                dfs(0,col, isBorder)
            if board[rows-1][col] == 'O':
                dfs(rows-1,col, isBorder)
        
        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row,0, isBorder)
            if board[row][cols-1] == 'O':
                dfs(row,cols-1, isBorder)
        isBorder = False
        for row in range(1,rows-1):
            for col in range(1,cols-1):
                if board[row][col] == 'O':
                    dfs(row,col,isBorder)



