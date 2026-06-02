class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for i in range(len(asteroids)):
            active = True

            while active and stack and stack[-1] > 0 and asteroids[i] < 0:

                if abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    active = False
                else:
                    active = False
            
            if active:
                stack.append(asteroids[i])
        
        return stack
                



            
            
                    

            