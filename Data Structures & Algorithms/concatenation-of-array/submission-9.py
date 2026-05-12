class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (2*len(nums))
        for i, v in enumerate(nums):
            res[i] = res[i+len(nums)] = nums[i]
        return res