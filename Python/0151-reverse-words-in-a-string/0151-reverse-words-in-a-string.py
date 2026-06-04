import re

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = re.sub(r"\s{2,}", " ", s)
        return ' '.join(s.strip().split(' ')[::-1])