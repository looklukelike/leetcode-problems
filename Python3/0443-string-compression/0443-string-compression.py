class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 1
        c = chars[0]
        count = 1
        while j < len(chars):
            if chars[j] != c:
                i += 1
                if count > 1:
                    for count_char in str(count):
                        chars[i] = count_char
                        i += 1
                c = chars[j]
                chars[i] = c
                count = 1
            elif chars[j] == c:
                count += 1
            j += 1

        if count > 1:
            for count_char in str(count):
                i += 1
                chars[i] = count_char
        
        return i + 1