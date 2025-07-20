"""
LeetCode Problem “Maximum Subarray” (https://leetcode.com/problems/maximum-subarray/)

Given an integer array `nums`, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Time Complexity: O(n)  
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        :param nums: List[int] – list of integers, possibly negative
        :return: int – the maximum sum of any contiguous subarray

        Approach (Kadane's Algorithm):
        1. Initialize `maximum` and `overall` to the first element.
        2. Iterate through the array starting at index 1:
           - Update `maximum` as the larger of the current element or
             `maximum + current element` (extend or start new subarray).
           - Update `overall` as the maximum of itself and `maximum`.
        3. Return `overall`, the largest subarray sum found.
        """
        # Handle empty input
        if not nums:
            return 0

        # `maximum` is max sum ending at current position; `overall` is max seen so far
        maximum = nums[0]
        overall = nums[0]

        # Iterate and update running and global maxima
        for i in range(1, len(nums)):
            maximum = max(nums[i], maximum + nums[i])
            overall = max(maximum, overall)

        return overall
