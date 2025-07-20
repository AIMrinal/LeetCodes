"""
LeetCode Problem “Convert 1D Array Into 2D Array” (https://leetcode.com/problems/convert-1d-array-into-2d-array/)

Given a 1D integer array `original` and two integers `m` and `n`, create a 2D array with `m` rows and
`n` columns by filling the elements of `original` in row-major order. If it is not possible, return an empty 2D array.

Time Complexity: O(m·n)  
Space Complexity: O(m·n)
"""

from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        """
        :param original: List[int] – the input 1D array
        :param m: int – desired number of rows
        :param n: int – desired number of columns
        :return: List[List[int]] – the filled 2D array or [] if dimensions mismatch

        Approach:
        1. Check if total elements m*n matches the length of original; if not, return [].
        2. Initialize an empty list `result` to hold the rows.
        3. For each row index i from 0 to m-1:
           - Slice the subarray from original[i*n : (i+1)*n].
           - Append it as the next row in result.
        4. Return the constructed 2D array.
        """
        # If the area doesn't match the number of elements, can't form a valid 2D array
        if (m * n) != len(original):
            return []

        result = []  # Will hold the rows of the 2D array

        # Build each row by slicing the appropriate segment from original
        for i in range(m):
            row = original[i * n : (i + 1) * n]
            result.append(row)

        return result
