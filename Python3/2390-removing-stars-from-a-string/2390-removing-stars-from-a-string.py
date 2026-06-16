class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c == '*':
                del stack[-1]
            else:
                stack.append(c)

        s = ''.join(stack)
        return s