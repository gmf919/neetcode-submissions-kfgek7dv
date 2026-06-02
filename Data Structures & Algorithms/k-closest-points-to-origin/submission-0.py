class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        minheap = []

        for x,y in points:
            distance = x*x + y*y

            minheap.append((distance,(x,y)))

        heapq.heapify(minheap)

        res = []

        for _ in range(k):
            dis,(x,y) = heapq.heappop(minheap)

            res.append((x,y))
        
        return res