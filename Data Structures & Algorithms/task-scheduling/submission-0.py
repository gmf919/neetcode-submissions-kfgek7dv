class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = collections.Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)

        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt,time + n])
            
            if queue and queue[0][1] == time:
                cnt, timer = queue.popleft()
                heapq.heappush(maxHeap, cnt)
        
        return time
            


            

