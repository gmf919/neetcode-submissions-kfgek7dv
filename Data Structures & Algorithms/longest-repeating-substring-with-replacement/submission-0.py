class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxCount = 0
        left = 0 
        count = {}
        res = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right],0) + 1
            maxCount = max(maxCount, count[s[right]])

            while (right - left + 1) - maxCount > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res




