"""
LeetCode Problem “Find All Numbers Disappeared in an Array” (https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

Given an array `nums` of size n where all elements are in the range [1, n], some elements appear twice
and others appear once. Return a list of all the integers in the range [1, n] that do not appear in `nums`.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        :param nums: List[int] – the input list containing numbers in [1, n] with possible duplicates
        :return: List[int] – all numbers in [1, n] missing from the list

        Approach:
        1. Build a set `s1` of the values present in `nums`.
        2. Build a set `s2` of all integers from 1 to n (where n = len(nums)).
        3. The difference `s2 - s1` yields exactly the missing numbers.
        """
        s1 = set(nums)
        s2 = set(i for i in range(1, len(nums) + 1))
        return list(s2 - s1)
