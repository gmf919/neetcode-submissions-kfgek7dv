class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        map = collections.Counter(nums)

        highest = 0
        ans = 0

        for key, val in map.items():

            if val > highest:
                highest = val
                ans = key
        
        return ans