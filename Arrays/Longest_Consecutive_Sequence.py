"""
LeetCode Problem “Longest Consecutive Sequence” (https://leetcode.com/problems/longest-consecutive-sequence/)

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

Time Complexity: O(n)  
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        :param nums: List[int] – the list of integers
        :return: int – length of the longest run of consecutive numbers

        Approach:
        1. Convert `nums` to a set `s` for O(1) lookups.
        2. For each number `n` in `s`, if `n-1` is not in `s`, it's the start of a sequence.
        3. Incrementally check `n+1, n+2, ...` to count the streak length.
        4. Keep track of the maximum streak found.
        """
        s = set(nums)         # enable constant-time membership checks
        longest = 0           # tracks the maximum consecutive sequence length

        for n in s:
            # only start a new count if `n` is the beginning of a sequence
            if n - 1 not in s:
                streak = 1
                # extend the streak while next numbers are present
                while n + streak in s:
                    streak += 1
                longest = max(longest, streak)

        return longest
