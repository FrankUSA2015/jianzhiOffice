# -*- coding: utf-8 -*-
class Solution:
    def maxValue(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]