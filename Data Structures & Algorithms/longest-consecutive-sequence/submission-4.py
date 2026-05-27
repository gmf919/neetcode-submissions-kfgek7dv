class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                x = num
                length = 1
                while x + 1 in numSet:
                    length += 1
                    x += 1
                longest = max(longest,length)
        
        return longest
            

