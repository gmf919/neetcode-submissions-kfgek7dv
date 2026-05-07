class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        
        rows = len(matrix)
        cols = len(matrix[0])

        firstRowzero = False
        firstColzero = False


        for col in range(cols):
            if matrix[0][col] == 0:
                firstRowzero = True

        for row in range(rows):
            if matrix[row][0] == 0:
                firstColzero = True

        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if firstRowzero:
            for col in range(cols):
                matrix[0][col] = 0
        
        if firstColzero:
            for row in range(rows):
                matrix[row][0] = 0

        

        
                


        