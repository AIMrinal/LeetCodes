"""
LeetCode Problem “Missing Number” (https://leetcode.com/problems/missing-number/)

Given an array `nums` containing `n` distinct numbers in the range [0, n], return the only number 
in the range that is missing from the array.

Time Complexity: O(n)  
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        :param nums: List[int] – list of distinct integers in [0, n] with one missing
        :return: int – the missing number in the range

        Approach:
        1. Compute the expected sum of all integers from 0 to n (where n = len(nums)).
        2. Subtract the actual sum of the input list from this expected sum.
        3. The difference is the missing number.
        """
        n = sum([i for i in range(0, len(nums) + 1)])  # expected total of 0..n
        actual = sum(nums)                             # actual total of elements present
        return n - actual                              # missing number
