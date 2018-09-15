class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2,-1,-1):
            for j in range(i+1):
                triangle[-1][j] = min(triangle[i][j]+triangle[-1][j],triangle[i][j]+triangle[-1][j+1])
        return triangle[-1][0]