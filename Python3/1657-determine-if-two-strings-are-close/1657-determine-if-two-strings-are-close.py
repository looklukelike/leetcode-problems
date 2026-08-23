class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1 = {}
        f2 = {}

        for letter in word1:
            if letter in f1:
                f1[letter] += 1
            else:
                f1[letter] = 1
        
        for letter in word2:
            if letter in f2:
                f2[letter] += 1
            else:
                f2[letter] = 1

        return sorted(f1.keys()) == sorted(f2.keys()) and sorted(f1.values()) == sorted(f2.values())