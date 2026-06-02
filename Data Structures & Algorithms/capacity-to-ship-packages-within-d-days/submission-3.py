class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l , r = max(weights) , sum(weights)
        res = r
        while l <= r:
            mid = (l + r) // 2
            ships = 1
            curr_cap = mid
            for w in weights:
                if curr_cap - w < 0:
                    ships += 1
                    curr_cap = mid
                curr_cap -= w
            
            if ships <= days:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res


            

                    
                    
                    
                