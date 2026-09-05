class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        res = nums[0]

        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            if val >= nums[0]:
                l = mid + 1
            else:
                res = val
                r = mid - 1

        return res
        