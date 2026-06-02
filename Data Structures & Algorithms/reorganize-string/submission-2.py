class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = collections.Counter(s)
        for val in counter.values():
            if (len(s) + 1) // 2 < val:
                return ''
        maxheap = [(-cnt,char) for char,cnt in counter.items()]

        heapq.heapify(maxheap)
        hold = None
        res = ''


        while maxheap:
            oldcnt, char = heapq.heappop(maxheap)
            res += char
            newcnt = 1 + oldcnt
            if hold:
                heapq.heappush(maxheap, hold)
                hold = None
            if newcnt:
                hold = (newcnt, char)
        
        return res

