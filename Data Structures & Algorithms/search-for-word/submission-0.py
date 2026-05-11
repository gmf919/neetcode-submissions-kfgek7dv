class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        if not board:
            return False


        def dfs(row, col, wordIndex):

            if wordIndex == len(word):
                return True
            

            if row < 0 or len(board) <= row or col < 0 or len(board[0]) <= col:
                return False
            
            if board[row][col] != word[wordIndex]:
                return False

            temp = board[row][col]
            board[row][col] = '!'

            found = (
                dfs(row + 1,col, wordIndex + 1) or
                dfs(row - 1,col, wordIndex + 1) or
                dfs(row,col + 1, wordIndex + 1) or
                dfs(row,col - 1, wordIndex + 1)
            )

            board[row][col] = temp

            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row,col,0):
                    return True

        return False


