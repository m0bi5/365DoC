class Solution:
    ugly = sorted([2**a * 3**b * 5**c for a in range(32) for b in range(20) for c in range(14)]) #generate all numbers with 2,3,5 as prime factors
    def nthUglyNumber(self, n):
        return Solution.ugly[n - 1] if n > 0 else None