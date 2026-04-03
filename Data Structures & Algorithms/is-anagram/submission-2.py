class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        smap = collections.Counter(s)
        tmap = collections.Counter(t)

        return smap == tmap
        