"""
LeetCode Problem “Subsets” (https://leetcode.com/problems/subsets/)

Given a list of unique integers `nums`, return all possible subsets (the power set).

Time Complexity: O(n·2ⁿ)  
Space Complexity: O(2ⁿ)
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        :param nums: List[int] – list of unique integers
        :return: List[List[int]] – all possible subsets of nums

        Approach:
        - Initialize `dp` with the empty subset.
        - For each element `x` in `nums`, create new subsets by adding `x` to each existing subset.
        - Extend `dp` with these new subsets to build the power set incrementally.
        """
        dp = [[]]  # start with the empty subset
        for x in nums:
            # build new subsets by appending x to each subset already in dp
            new_subsets = [curr + [x] for curr in dp]
            dp += new_subsets  # add them to the list of all subsets
        return dp
