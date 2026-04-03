class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        n = sorted(counter.keys(), key=counter.get, reverse=True)
        print(n)
        return n[:k]
