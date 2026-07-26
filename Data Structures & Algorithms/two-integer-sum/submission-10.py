class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_idx = {}
        for idx, val in enumerate(nums):
            to_check = target - val
            if to_check in val_to_idx: return [val_to_idx[to_check], idx]
            val_to_idx[val] = idx
        return []