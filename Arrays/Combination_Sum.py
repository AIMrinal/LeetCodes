"""
LeetCode Problem “Combination Sum” (https://leetcode.com/problems/combination-sum/)

Given a list of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations
of `candidates` where the chosen numbers sum to `target`. You may use each candidate an unlimited number of times.
The solution set must not contain duplicate combinations.

Time Complexity: Exponential in the worst case (branching factor up to len(candidates), depth up to target/min(candidates))  
Space Complexity: O(target/min(candidates)) for recursion stack plus the space required for results
"""

from typing import List

class Solution:
    def helper(self, start: int, remaining: int, path: List[int],
               candidates: List[int], res: List[List[int]]) -> None:
        """
        Backtracking helper to build combinations.

        :param start:    index in `candidates` to start choosing from (prevents reordering duplicates)
        :param remaining: int – amount left to reach the target sum
        :param path:     List[int] – current combination being built
        :param candidates: List[int] – sorted list of available numbers
        :param res:      List[List[int]] – accumulator for valid combinations
        """
        # If we've hit the target, record a copy of the current path
        if remaining == 0:
            res.append(path.copy())
            return

        # Try each candidate from `start` onward
        for i in range(start, len(candidates)):
            c = candidates[i]
            # If the candidate exceeds remaining, no need to continue (sorted list)
            if c > remaining:
                break
            # Choose candidate c
            path.append(c)
            # Recurse with updated remaining and same index i (allow reuse)
            self.helper(i, remaining - c, path, candidates, res)
            # Backtrack: remove last choice
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :param candidates: List[int] – distinct positive integers
        :param target:     int – target sum to achieve with combinations
        :return:           List[List[int]] – all unique combinations summing to target

        Approach:
        1. Sort `candidates` to enable early stopping when a candidate > remaining.
        2. Use backtracking (`helper`) starting at index 0 with an empty path.
        3. For each position, either include the candidate (and stay at same index) or skip it.
        4. Collect each valid path when remaining == 0.
        """
        candidates.sort()          # sort to allow pruning
        res: List[List[int]] = []  # list to hold all valid combinations
        self.helper(0, target, [], candidates, res)
        return res
