class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # approach-1:   
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid//COLS][mid%COLS]
            if val < target:
                l = mid + 1
            elif target < val:
                r = mid - 1
            else: return True
        return False