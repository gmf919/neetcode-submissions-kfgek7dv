class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = collections.defaultdict(list)

        for string in strs:
            hashmap[tuple(sorted(string))].append(string)
        
        return hashmap.values()

