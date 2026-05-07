class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        dic = {
            ")":"(",
            "}":"{",
            "]": "["
        }

        for op in s:
            if op in dic.values():
                stack.append(op)
            else:
                if stack and stack[-1] == dic[op]:
                    stack.pop()
                else:
                    return False

        
        return not stack

            

            

