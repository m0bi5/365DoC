class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        rec = [0]*n
        maximum = 0
        prev = 0
        for i in range(m):
            for j in range(n):
                temp = rec[j]
                if matrix[i][j] == "1":
                    if j > 0:
                        rec[j] = min(rec[j-1],rec[j],prev)+1
                    else:
                        rec[j] = 1
                else:
                    rec[j] = 0
                prev = temp
                maximum = max(maximum,rec[j])
        return maximum*maximum