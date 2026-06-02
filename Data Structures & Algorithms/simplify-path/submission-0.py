class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = path.split('/')

        stack = []

        for c in curr:

            if c == '' or c == '.':
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
            
        res = ''
        for s in stack:
            res += '/' + s
        
        return res if res != '' else '/'


        
            

