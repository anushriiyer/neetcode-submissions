class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = rows-1

        while low<=high:
            mid = low + (high-low)//2

            if target in matrix[mid]:
                return True
            
            elif target< matrix[mid][0]:
                high = mid-1
            
            elif target> matrix[mid][0]:
                low = mid+1
        
        return False

            

        