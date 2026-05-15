class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            while l <= r and nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            if l > r: break
            l += 1

        return l