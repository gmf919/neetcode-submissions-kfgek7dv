class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        maxheap = []
        for cnt, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heapq.heappush(maxheap, (cnt, char))

        res = ''

        while maxheap:

            curr_cnt, char = heapq.heappop(maxheap)

            if len(res) >= 2 and res[-1] == res[-2] == char:
                if maxheap: 
                    curr_cnt2, char2 = heapq.heappop(maxheap)
                    res += char2
                    heapq.heappush(maxheap,(curr_cnt,char))
                    if curr_cnt2 + 1 < 0:
                        heapq.heappush(maxheap,(curr_cnt2 + 1,char2))
                else:
                    return res
            else:
                res += char
                if curr_cnt + 1 < 0:
                    heapq.heappush(maxheap,(curr_cnt + 1,char))
        
        return res


