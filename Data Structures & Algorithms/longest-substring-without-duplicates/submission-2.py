class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxlen = 0
        res = set()
        left = 0

        for right in range(len(s)):

            while s[right] in res:
                res.remove(s[left])
                left += 1
            
            res.add(s[right])
            
            maxlen = max(maxlen, right - left + 1)
        
        return maxlen
  
        




            