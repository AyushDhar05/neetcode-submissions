class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        frequency = defaultdict(int)
        for i, j in zip(s, t):
            frequency[i] += 1
            frequency[j] -= 1
        return len(set(frequency.values())) == 1