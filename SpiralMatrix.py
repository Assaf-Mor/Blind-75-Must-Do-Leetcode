class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        leftP, rightP = 0, len(matrix[0])
        topP, bottomP = 0, len(matrix)

        while rightP > leftP and topP < bottomP:
            for i in range(leftP, rightP):
                result.append(matrix[topP][i])
            topP += 1
            for i in range (topP, bottomP):
                result.append(matrix[i][rightP - 1])
            rightP -=1

            if not (leftP < rightP and topP < bottomP):
                break;

            for i in range (rightP - 1,leftP - 1, -1):
                result.append(matrix[bottomP - 1][i])
            bottomP -= 1
            for i in range(bottomP - 1, topP - 1, -1):
                result.append(matrix[i][leftP])
            leftP += 1
        return result

