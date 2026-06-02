class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        combined = list(zip(position,speed))

        combined.sort(key= lambda x : x[0], reverse = True)

        for car in combined:
            arrivaltime = (target - car[0]) / car[1]
            if stack and arrivaltime <= stack[-1]:
                continue
            stack.append(arrivaltime)
        
        return len(stack)