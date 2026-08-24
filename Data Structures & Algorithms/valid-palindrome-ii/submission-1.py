class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1


        def helper(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l, r = l + 1, r - 1
            return True



        while l < r:
            if s[l] != s[r]:
                return helper(l+1, r) or helper(l, r-1)
            else:
                l, r = l + 1, r - 1
        
        return True