class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h = collections.defaultdict()

        for i,num in enumerate(nums):
            if (target - num) in h:
                return [h[target-num],i]
            h[num] = i