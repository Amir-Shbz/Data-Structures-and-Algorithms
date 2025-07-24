# 1030

# You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and 
# you are on the cell with the coordinates (rCenter, cCenter).

# Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) 
# from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

# The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.

import collections

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:

        d = collections.defaultdict(list)
        res = []
        for i in range(rows):
            for j in range(cols):
                distance = abs(rCenter-i)+abs(cCenter-j)
                d[distance].append([i,j])

        for i in sorted(d):
            res += d[i] 

        return res   

