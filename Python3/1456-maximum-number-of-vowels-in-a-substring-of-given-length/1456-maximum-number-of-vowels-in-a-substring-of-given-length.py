class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        j = k
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_vowels = 0

        window = s[:k]
        for idx in range(k):
            if window[idx] in vowels:
                max_vowels += 1

        print(window)

        j += 1
        counter = max_vowels
        while j <= len(s):
            if s[j - 1] in vowels:
                counter += 1
            if s[j - k - 1] in vowels:
                counter -= 1
            max_vowels = max(counter, max_vowels)
            j += 1

        
        return max_vowels 