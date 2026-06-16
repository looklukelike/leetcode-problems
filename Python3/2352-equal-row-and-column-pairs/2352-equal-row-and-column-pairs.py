class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = []
        rows = []
        for i in range(len(grid)):
            columns.append([])
            rows.append([])
            for j in range(len(grid)):
                columns[-1].append(grid[j][i])
                rows[-1].append(grid[i][j])

        total = 0
        for row in rows:
            for column in columns:
                if row == column:
                    total += 1

        return total