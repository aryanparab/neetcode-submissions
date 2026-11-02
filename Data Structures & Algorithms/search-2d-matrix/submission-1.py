class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)
        while l<r:
            mid = (l+r)//2
            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                for i in matrix[mid]:
                    if i==target:
                        return True
                return False
            if matrix[mid][0]>target:
                r = mid
            else:
                l= mid+1
        return False