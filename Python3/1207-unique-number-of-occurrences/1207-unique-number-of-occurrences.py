class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict()

        for value in arr:
            if value in d:
                d[value] += 1
            else:
                d[value] = 0

        return len(set(d.values())) == len(d.values())