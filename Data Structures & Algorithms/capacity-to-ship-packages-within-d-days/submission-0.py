class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = sum(weights)
        l, r = max(weights), sum(weights)

        def time_taken(cap):
            ships = 0
            curr = 0
            for w in weights:
                if curr + w > cap:
                    ships += 1
                    curr = 0
                curr += w

            return ships + (1 if curr else 0) 

        while l <= r:
            mid = (l + r) // 2
            val = time_taken(mid)
            if val <= days:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res