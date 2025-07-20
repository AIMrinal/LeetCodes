"""
LeetCode Problem “Set Matrix Zeroes” (https://leetcode.com/problems/set-matrix-zeroes/)

Given an m x n matrix, if an element is 0, set its entire row and column to 0s.
Do it in-place.

Time Complexity: O(m·n)
Space Complexity: O(m + n)
"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        :param matrix: List[List[int]] – the m×n matrix to modify in-place
        :return: None – the matrix is updated directly

        Approach:
        1. First pass: record all rows and columns that contain at least one zero.
        2. Second pass: for each cell, if its row or column is marked, set it to zero.
        """
        m = len(matrix)
        n = len(matrix[0])

        row = set()  # rows to be zeroed
        col = set()  # columns to be zeroed

        # Identify rows and columns that must be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        # Zero out marked rows and columns
        for i in range(m):
            for j in range(n):
                if i in row:
                    # zero entire row
                    matrix[i][j] = 0
                else:
                    if j in col:
                        # zero column in non-marked row
                        matrix[i][j] = 0
