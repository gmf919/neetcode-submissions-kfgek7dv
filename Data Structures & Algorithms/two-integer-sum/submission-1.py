class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i,val in enumerate(nums):

            remainder = target - val
            if remainder in map.keys():
                return [map[remainder], i]
            
            map[val] = i

    