class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ansLen = 2 * len(nums)
        ans = [0] * ansLen

        for n in range(ansLen):

            ans[n] = nums[n % len(nums)]

        return ans

        


            