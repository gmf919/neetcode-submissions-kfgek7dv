class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for val in counter.values():
            if val > 1:
                return True
        
        return False
