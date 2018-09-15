class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = set()
        pre = set()
        for n in A:
            cur = set([n])
            for p in pre:
                cur.add(p|n)
            pre = cur
            for p in pre:
                res.add(p)
        return len(res)