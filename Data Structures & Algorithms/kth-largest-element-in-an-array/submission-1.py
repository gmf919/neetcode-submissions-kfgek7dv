class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)

        while nums:
            if len(nums) == k:
                return heapq.heappop(nums)
            
            heapq.heappop(nums)