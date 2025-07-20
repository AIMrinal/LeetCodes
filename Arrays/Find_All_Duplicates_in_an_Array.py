"""
LeetCode Problem “Find All Duplicates in an Array” (https://leetcode.com/problems/find-all-duplicates-in-an-array/)

Given an integer array `nums` of length n where all elements are in the range [1, n],
some elements appear twice and others appear once. Return a list of all the elements that appear twice.

Time Complexity: O(n)  
Space Complexity: O(1) extra space (excluding the output list)
"""

from typing import List
from collections import Counter  # imported for reference but not used in this approach

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        :param nums: List[int] – the input list containing numbers in [1, n] with possible duplicates
        :return: List[int] – all numbers that appear twice in the list

        Approach:
        1. Iterate through each number `x` in `nums`.
        2. Use the value `abs(x) - 1` as an index to mark visits by flipping the sign at `nums[index]`.
        3. If `nums[index]` is positive, flip it to negative to mark that the number has been seen.
        4. If `nums[index]` is already negative, the number `index+1` is a duplicate; add to result list.
        """
        n = len(nums)
        r = []  # result list for duplicates

        for i in range(n):
            index = abs(nums[i]) - 1  # map value to index
            if nums[index] > 0:
                # First time seeing this number: mark as seen by negating
                nums[index] = -nums[index]
            else:
                # Already marked: this number is a duplicate
                r.append(index + 1)

        return r
