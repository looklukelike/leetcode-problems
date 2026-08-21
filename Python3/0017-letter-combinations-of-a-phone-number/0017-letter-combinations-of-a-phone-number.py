import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_digits = {
            2: list('abc'),
            3: list('def'),
            4: list('ghi'),
            5: list('jkl'),
            6: list('mno'),
            7: list('pqrs'),
            8: list('tuv'),
            9: list('wxyz')
        }

        combs = []
        for digit in digits:
            digit = int(digit)
            if len(combs) == 0:
                for c in phone_digits[digit]:
                    combs.append(c)
                    continue
            else:
                _temp = []
                for comb in combs:
                    for c in phone_digits[digit]:
                        chunk = comb + c
                        _temp.append(chunk)
                combs = _temp

        return combs

