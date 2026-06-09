class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        j = k - 1
        vowels = set('aeiou')
        max_vowels = 0

        window = s[:k]
        for idx in range(k):
            if window[idx] in vowels:
                max_vowels += 1

        j += 1
        counter = max_vowels
        while j < len(s):
            if s[j] in vowels:
                counter += 1
            if s[j - k] in vowels:
                counter -= 1
            max_vowels = max(counter, max_vowels)
            j += 1

        
        return max_vowels 