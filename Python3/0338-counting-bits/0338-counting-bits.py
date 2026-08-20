class Solution:
    def countBits(self, n: int) -> List[int]:

        def binaryFormCountOnes(x: int) -> tuple(str, int):
            count = 0
            while x > 0:
                count += 1 if x % 2 == 1 else 0
                x = x // 2
            return count
            
        l = []
        for n in range(n + 1):
            l.append(binaryFormCountOnes(n))

        return l