class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            if val == target: return mid
            if val >= nums[0]: #left
                if nums[l] <= target <= val:
                    r = mid - 1
                else: l = mid + 1
            else:
                if val <= target <= nums[-1]:
                    l = mid + 1
                else: r = mid - 1
        return -1