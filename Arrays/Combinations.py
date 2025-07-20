"""
LeetCode Problem “Combinations” (https://leetcode.com/problems/combinations/)

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

Time Complexity: O(k · C(n, k)) — each combination of length k is built in O(k) time  
Space Complexity: O(k · C(n, k)) — storing all combinations
"""

from typing import List

class Solution:
    def helper(self, s: int, n: int, k: int) -> List[List[int]]:
        """
        Recursive helper to build combinations.
        
        :param s: int – starting number for this recursion level
        :param n: int – upper bound of numbers (inclusive)
        :param k: int – remaining length of combinations to build
        :return: List[List[int]] – list of combinations of length k from [s, n]
        
        Approach:
        - Iterate i from s to n.
        - For k == 2, directly pair i with each subsequent number j > i.
        - Otherwise, recursively build combinations of size k-1 starting from i+1,
          then prepend i to each sub-combination.
        """
        res = []
        for i in range(s, n + 1):
            temp = [i]
            if k == 2:
                # Base-case: pick one more number j > i to complete pairs
                for j in range(i + 1, n + 1):
                    res.append(temp + [j])
            else:
                # Recursive case: build remaining k-1 elements
                subset = self.helper(i + 1, n, k - 1)
                for sfx in subset:
                    res.append(temp + sfx)
        return res

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        :param n: int – the upper bound of the range [1, n]
        :param k: int – the size of each combination
        :return: List[List[int]] – all possible combinations of k numbers from [1, n]
        
        Approach:
        - Handle edge cases:
          • If k == n, only one combination: [1, 2, ..., n].
          • If k == 1, each number from 1 to n is its own combination.
        - Otherwise, delegate to helper starting at 1.
        """
        # If k == n, the only combination is the full range
        if n == k:
            return [[i for i in range(1, n + 1)]]
        # If k == 1, each single number is a valid combination
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        # General case
        return self.helper(1, n, k)
