# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        bounds = [0, n + 1]
        val = (n + 1)// 2
        while True:
            ans = guess(val)
            if ans == 1:
                bounds[0] = val
                val += (bounds[1] - bounds[0]) // 2
            elif ans == -1:
                bounds[1] = val
                val -= (bounds[1] - bounds[0]) // 2
            else:
                break
        
        return val
