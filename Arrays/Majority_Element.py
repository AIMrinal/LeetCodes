"""
LeetCode Problem “Majority Element” (https://leetcode.com/problems/majority-element/)

Given an array `nums` of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        :param nums: List[int] – the list of input integers
        :return: int – the element that appears more than n/2 times

        Approach:
        1. Use Counter to build a frequency map of all elements in O(n).
        2. Sort the (element, count) pairs by count descending in O(n log n).
        3. The first element of the sorted list is the majority element.
        """
        # Step 1: Build frequency map
        d = Counter(nums)
        # Step 2: Sort items by frequency in descending order
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        # Step 3: Return the element with the highest frequency
        return list(d.items())[0][0]
