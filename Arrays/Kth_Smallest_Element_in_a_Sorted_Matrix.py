"""
LeetCode Problem “Kth Smallest Element in a Sorted Matrix” (https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

Given an n x n matrix where each of the rows and columns is sorted in ascending order, 
return the kᵗʰ smallest element in the matrix.

Time Complexity: O(n² log n²) = O(n² log n)  
Space Complexity: O(n²)
"""

from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        :param matrix: List[List[int]] – n×n matrix with each row and column sorted
        :param k: int – the 1-based rank of the smallest element to retrieve
        :return: int – the kᵗʰ smallest element in the flattened matrix
        """
        s = []  # will hold all elements of the matrix
        n = len(matrix)  # dimension of the square matrix

        # Flatten the matrix into list s
        for i in range(0, n):
            for j in range(0, n):
                s.append(matrix[i][j])

        # Sort all elements in ascending order
        s = sorted(s)

        # Return the element at index k-1 (since k is 1-based)
        return s[k-1]
