"""
LeetCode Problem “Rotate Image” (https://leetcode.com/problems/rotate-image/)

Given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You must rotate the image in-place without allocating another matrix.

Time Complexity: O(n²)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        :param matrix: List[List[int]] – the n×n image to rotate in-place
        :return: None – modifies the input matrix directly

        Approach:
        1. Transpose the matrix by swapping elements across the diagonal:
           - For each i from 0 to n−1, for each j from i+1 to n−1,
             swap matrix[i][j] with matrix[j][i].
        2. Reverse each row to complete the 90° clockwise rotation.
        """
        n = len(matrix)
        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Step 2: Reverse rows
        for i in range(n):
            matrix[i].reverse()
