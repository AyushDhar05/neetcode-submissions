class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        seen_map = {}
        for ch1, ch2 in zip(s, t):
            seen_map[ch1] = seen_map.get(ch1, 0) + 1
            seen_map[ch2] = seen_map.get(ch2, 0) - 1

        for v in seen_map.values():
            if v != 0: 
                return False
        
        return True