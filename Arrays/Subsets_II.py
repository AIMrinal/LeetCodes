"""
LeetCode Problem “Subsets II” (https://leetcode.com/problems/subsets-ii/)

Given a collection of integers `nums` that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.

Time Complexity: O(n·2ⁿ)  
Space Complexity: O(2ⁿ)
"""

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        :param nums: List[int] – list of integers that may include duplicates
        :return: List[List[int]] – all unique subsets of nums

        Approach:
        1. Sort `nums` to group duplicates together.
        2. Initialize `dp` with the empty subset.
        3. Track `start`, the size of `dp` before processing the current element.
        4. For each index `i`:
           - If `nums[i]` is the same as the previous element, only build new subsets
             from those added in the last iteration (from `start` to current length).
           - Otherwise, build from all existing subsets.
        5. Append each newly formed subset (existing subset + `nums[i]`) to `dp`.
        """
        dp = [[]]               # start with the empty subset
        start = 0               # boundary for duplicates handling
        n = len(nums)
        nums = sorted(nums)     # sort to bring duplicates together

        for i in range(n):
            # Determine where to start when handling duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                i_start = start
            else:
                i_start = 0
            # Update start to current dp size before adding new subsets
            start = len(dp)
            # Build new subsets by extending appropriate range of dp
            for subset in dp[i_start:start]:
                dp.append(subset + [nums[i]])

        return dp
