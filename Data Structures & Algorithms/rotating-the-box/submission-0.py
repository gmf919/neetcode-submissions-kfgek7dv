class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for row in range(rows):
            empty_position = cols - 1
            for col in range(cols - 1,-1,-1):
                
                if boxGrid[row][col] == '*':

                    empty_position = col - 1

                if boxGrid[row][col] == '#':

                    boxGrid[row][col] = '.'
                    boxGrid[row][empty_position] = '#'
                    empty_position -= 1

        rotated = []

        for col in range(cols):
            newrow = []
            for row in range(rows-1,-1,-1):
                newrow.append(boxGrid[row][col])

            rotated.append(newrow)

        return rotated

