"""
LeetCode Problem “Remove Element” (https://leetcode.com/problems/remove-element/)

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place and return the new length.
You must do this with O(1) extra memory and modify the input array directly.

Time Complexity: O(n²) in the worst case (each `.remove()` is O(n) and may occur up to n times)  
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        :param nums: List[int] – the list of input integers
        :param val: int – the value to remove from nums
        :return: int – the length of nums after removing all occurrences of val
        """
        while (val in nums):
            nums.remove(val)
        return len(nums)
