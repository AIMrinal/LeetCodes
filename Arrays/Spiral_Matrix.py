"""
LeetCode Problem “Spiral Matrix” (https://leetcode.com/problems/spiral-matrix/)

Given an m x n matrix, return all elements of the matrix in spiral order.

Time Complexity: O(m·n)
Space Complexity: O(1) extra space (excluding the output list)
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        :param matrix: List[List[int]] – the input 2D matrix
        :return: List[int] – elements in spiral (clockwise) order

        Approach:
        1. Maintain four boundaries: top, bottom, left, right.
        2. Traverse the top row from left→right, then increment top.
        3. Traverse the right column from top→bottom, then decrement right.
        4. If top≤bottom, traverse the bottom row from right→left, then decrement bottom.
        5. If left≤right, traverse the left column from bottom→top, then increment left.
        6. Repeat until boundaries cross.
        """
        if not matrix:
            # Empty matrix → no elements
            return []
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        spiral = []  # result list

        # Continue until the boundaries cross
        while top <= bottom and left <= right:

            # Traverse top row
            for col in range(left, right + 1):
                spiral.append(matrix[top][col])
            top += 1  # move top boundary down

            # Traverse right column
            for row in range(top, bottom + 1):
                spiral.append(matrix[row][right])
            right -= 1  # move right boundary left

            # Traverse bottom row if still valid
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][col])
                bottom -= 1  # move bottom boundary up

            # Traverse left column if still valid
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    spiral.append(matrix[row][left])
                left += 1  # move left boundary right

        return spiral
