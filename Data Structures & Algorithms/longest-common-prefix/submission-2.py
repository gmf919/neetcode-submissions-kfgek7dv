class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ''

        pre = ''

        for i in range(len(strs[0])):
            for s in strs[1:]:
                if (len(s) - 1) < i or strs[0][i] != s[i]:
                    return pre
            pre += strs[0][i]

        return strs[0]
