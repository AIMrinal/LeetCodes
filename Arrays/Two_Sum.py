"""
solution.py

LeetCode Problem “Two Sum” (https://leetcode.com/problems/two-sum/)

Given a list of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`. Assumes exactly one
solution exists and you may not use the same element twice.

Time Complexity: O(n)
Space Complexity: O(n)

"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums: List[int] – the list of input integers
        :param target: int – the target sum
        :return: List[int] – a list containing the two indices [i, j]
        """
        d = {}  # Map each number seen so far to its index
        for index, value in enumerate(nums):
            diff = target - value  # Complementary value needed to reach target
            if diff in d:
                # Found the pair: current index and stored index of diff
                return [index, d[diff]]
            else:
                # Record the current number and its index
                d[value] = index
