"""
LeetCode Problem “Single Number” (https://leetcode.com/problems/single-number/)

Given a non-empty array of integers `nums`, every element appears twice except for one.
Find that single one.

Time Complexity: O(n)  
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        :param nums: List[int] – the list of integers where every element appears twice except one
        :return: int – the element that appears only once

        Approach:
        1. Initialize a result variable `res` to 0.
        2. XOR each number in `nums` with `res`. Since x ^ x = 0 and x ^ 0 = x,
           all paired numbers cancel out, leaving only the single number.
        3. Return `res`.
        """
        res = 0
        for n in nums:
            res = res ^ n
        return res
