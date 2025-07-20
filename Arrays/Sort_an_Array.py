"""
LeetCode Problem “Sort an Array” (https://leetcode.com/problems/sort-an-array/)

Given an integer array `nums`, return the array sorted in ascending order.

Time Complexity: O(n log n)  
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def merge(self, left, right):
        """
        Merge two sorted lists into one sorted list.

        :param left: List[int] – first sorted subarray
        :param right: List[int] – second sorted subarray
        :return: List[int] – merged sorted array
        """
        i = j = 0
        merged = []
        # Compare elements from left and right, appending the smaller to merged
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # Append any remaining elements from either subarray
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sort an array using merge sort.

        :param nums: List[int] – the input array to sort
        :return: List[int] – the sorted array
        """
        # Base case: a single element (or empty) list is already sorted
        if len(nums) <= 1:
            return nums
        # Divide the array into two halves
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        # Conquer: merge the sorted halves
        return self.merge(left, right)
