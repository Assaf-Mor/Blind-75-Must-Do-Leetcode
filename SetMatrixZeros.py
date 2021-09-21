class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        isFirstRowZero = False

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        isFirstRowZero = True
        
        for r in range(1,row):
            for c in range(1,col):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] == 0

        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0
        
        if isFirstRowZero:
            for c in range(col):
                matrix[0][c] = 0

        print(matrix)


if __name__ == "__main__":
    sol = Solution()
    sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
        
        
        
        