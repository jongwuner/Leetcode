class Solution:
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            # Go right
            result += matrix.pop(0)
            
            if matrix and matrix[0]: # Check if matrix is not empty
                # Go down
                for row in matrix:
                    result.append(row.pop())
                
            if matrix: # Check if matrix is not empty
                # Go left
                result += matrix.pop()[::-1]
            
            if matrix and matrix[0]: # Check if matrix is not empty
                # Go up
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        
        return result