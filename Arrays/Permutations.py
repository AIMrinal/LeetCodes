"""
LeetCode Problem “Permutations” (https://leetcode.com/problems/permutations/)

Given a list of distinct integers `nums`, return all possible permutations.
You may return the answer in any order.

Time Complexity: O(n · n!) — generating n! permutations, each of length n  
Space Complexity: O(n · n!) — storing all permutations in the result list
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        :param nums: List[int] – list of distinct integers to permute
        :return: List[List[int]] – list of all possible permutations

        Approach:
        - Use recursion and list-copying to build permutations.
        - Base cases handle lists of length 1 and 2 directly.
        - For longer lists, pick each element in turn as the first element,
          then recursively permute the remaining elements and prepend the picked element.
        """
        res = []
        # Base case for two elements: return both orders
        if len(nums) == 2:
            res.append(nums)
            res.append(nums[::-1])
            return res
        # Base case for a single element: only one permutation
        elif len(nums) == 1:
            res.append(nums)
            return res

        # Recursive case: build permutations by choosing each element in turn
        for i in range(len(nums)):
            temp = nums.copy()           # copy the list for safe removal
            subset = [temp.pop(i)]       # pick the i-th element as the first in permutation
            if len(temp) == 2:
                # if two elements remain, use the base-case logic to append both orders
                res.append(subset + temp)
                res.append(subset + temp[::-1])
            else:
                # otherwise, recursively permute the remaining list
                sub_perms = self.permute(temp)
                for s in sub_perms:
                    res.append(subset + s)

        return res
