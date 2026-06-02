class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l , r = 1 , max(piles)
        res = r

        while l <= r:

            speed = (l + r) // 2

            total_time = 0

            for pile in piles:
                total_time += math.ceil(pile / speed)
            
            if total_time <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1
        return res
