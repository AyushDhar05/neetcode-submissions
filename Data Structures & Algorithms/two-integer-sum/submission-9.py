class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        
        for i, v in enumerate(nums):
            if target - v in seen_map:
                return [seen_map[target - v], i]
            seen_map[v] = i

        return [0,0]