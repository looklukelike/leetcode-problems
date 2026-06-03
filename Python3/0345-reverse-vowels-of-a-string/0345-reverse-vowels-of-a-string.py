class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        l = []
        i = j = -1
        while i < len(s) - 1:
            i += 1
            if s[i] in vowels:
                l.append(s[i])
                j += 1
        i = 0
        while i < len(s):
            if s[i] in vowels:
                s[i] = l.pop()
            i += 1
        
        return ''.join(s)
