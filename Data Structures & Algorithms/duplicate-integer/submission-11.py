class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = set()
        for num in nums:
            seen_set.add(num)
        return True if len(seen_set) != len(nums) else False