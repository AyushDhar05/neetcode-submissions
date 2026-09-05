class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l, r = 1, max(piles)
        rate = max(piles)

        def banana_time(speed):
            time = 0
            for p in piles:
                time += math.ceil(p/speed)
            return time


        while l <= r:
            mid = (l + r) // 2
            val = banana_time(mid)
            if val <= h:
                rate = min(rate, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return rate

        