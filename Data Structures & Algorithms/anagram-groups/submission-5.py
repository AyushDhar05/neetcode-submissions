class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            chars = [0] * 26
            for ch in s:
                chars[ord(ch) - ord('a')] += 1
            
            chars_tuple = tuple(chars)

            if chars_tuple not in res:
                res[chars_tuple] = []
            
            res[chars_tuple].append(s)

        return list(res.values())