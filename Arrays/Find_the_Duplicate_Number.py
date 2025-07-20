"""
LeetCode Problem “Find the Duplicate Number” (https://leetcode.com/problems/find-the-duplicate-number/)

Given a list of integers `nums` containing n + 1 integers where each integer is between 1 and n (inclusive),
there is only one duplicate number but it could be repeated more than once. Return the duplicate number.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        :param nums: List[int] – the list of integers containing one duplicate
        :return: int – the duplicate number found in the list

        Approach:
        - Use a set to keep track of numbers we've seen so far.
        - Iterate through the list:
          • If the number is not in the set, add it.
          • If it is already in the set, we have found the duplicate; return it.
        """
        s = set()  # Set to store seen numbers
        for i in nums:
            if(i not in s):
                # Number not seen yet: record it
                s.add(i)
            else:
                # Number already seen: duplicate identified
                return i
