class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        i, j = 0, n-1
        while i <= j:
            mid = (i+j)//2
            if target > matrix[mid][-1]:
                i = mid+1
            elif target < matrix[mid][0]:
                j = mid-1
            else:
                break
        
        if not i <= j:
            return False
        row = (i+j)//2
        l, r = 0, m-1
        while l <= r:
            mid = (l+r)//2
            if target > matrix[row][mid]:
                l = mid+1
            elif target < matrix[row][mid]:
                r = mid-1
            else:
                return True
        return False
       

        