class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = x
        while l <= r:
            mid = (l + r) // 2
            val = mid * mid
            if val < x:
                res = mid
                l = mid + 1
            elif x < val:
                r = mid - 1
            else:
                return mid
        return res