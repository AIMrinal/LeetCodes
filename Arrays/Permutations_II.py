"""
LeetCode Problem “Permutations II” (https://leetcode.com/problems/permutations-ii/)

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Time Complexity: O(n · n!) in the worst case  
Space Complexity: O(n · n!) for storing all unique permutations
"""

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        :param nums: List[int] – list of integers that may include duplicates
        :return: List[List[int]] – all unique permutations of nums

        Approach:
        - Use recursion and list-copying to build permutations.
        - Handle base cases for lists of length 1 and 2, avoiding duplicates.
        - For longer lists, pick each element as the first element in turn,
          recursively permute the remaining elements, and prepend the picked element,
          checking for uniqueness before appending.
        """
        res = []  # stores all unique permutations

        # Base case: two elements — add both orders if not already added
        if len(nums) == 2:
            if nums not in res:
                res.append(nums)
            if nums[::-1] not in res:
                res.append(nums[::-1])
            return res

        # Base case: single element — only one permutation
        if len(nums) == 1:
            res.append(nums)
            return res

        # Recursive case: build permutations by choosing each element
        for i in range(len(nums)):
            temp = nums.copy()        # copy list to remove element safely
            first = [temp.pop(i)]     # select the i-th element as the leading element

            if len(temp) == 2:
                # for two remaining elements, form both orders, checking uniqueness
                perm1 = first + temp
                perm2 = first + temp[::-1]
                if perm1 not in res:
                    res.append(perm1)
                if perm2 not in res:
                    res.append(perm2)
            else:
                # recursively permute the rest of the list
                for suffix in self.permuteUnique(temp):
                    candidate = first + suffix
                    if candidate not in res:
                        res.append(candidate)

        return res
