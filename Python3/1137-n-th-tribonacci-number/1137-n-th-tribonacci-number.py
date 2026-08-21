class Solution:
    def tribonacci(self, n: int) -> int:
        n0 = 0
        n1 = 1
        n2 = 1
        if n == 0: return 0

        i = 2
        while i < n:
            _tmp0 = n0
            _tmp1 = n1
            n0 = n1
            n1 = n2
            n2 += _tmp0 + _tmp1
            i += 1

        return n2