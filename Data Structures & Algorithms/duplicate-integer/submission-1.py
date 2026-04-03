class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash = collections.Counter(nums)

        for val in hash.values():
            if val > 1:
                return True

        return False