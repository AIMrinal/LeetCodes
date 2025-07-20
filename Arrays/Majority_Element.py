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
        d = Counter(nums)
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        return list(d.items())[0][0]
