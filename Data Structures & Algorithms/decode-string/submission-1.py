class Solution:
    def decodeString(self, s: str) -> str:
        

        stack = []

        for c in s:

            if c != ']':
                stack.append(c)
            else:

                substring = ''
                while stack and stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()

                n = ''
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                
                stack.append(int(n) * substring)

        return ''.join(stack)

        