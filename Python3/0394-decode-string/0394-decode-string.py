class Solution:
    def decodeString(self, s: str) -> str:
        letters_stack = ['']
        num_stack = [1]
        i = 0
        while i < len(s):
            c = s[i]
            if c.isnumeric():
                j = i + 1
                while j < len(s):
                    if not s[j].isnumeric():
                        break
                    j += 1
                num_stack.append(int(s[i:j]))
                i = j - 1
            elif c =='[':
                letters_stack.append('')
            elif c == ']':
                new = letters_stack.pop() * num_stack.pop()
                letters_stack[-1] += new
            else:
                letters_stack[-1] += c

            i += 1

        return ''.join(letters_stack)
