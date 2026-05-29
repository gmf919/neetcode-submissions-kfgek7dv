class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Counter = collections.Counter(s1)

        l,r = 0 , len(s1)

        while r <= len(s2):

            currCounter = collections.Counter(s2[l:r])

            if currCounter == s1Counter:
                return True
            
            l+= 1
            r+= 1
        
        return False
        

