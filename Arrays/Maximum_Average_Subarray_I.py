"""
LeetCode Problem “Maximum Average Subarray I” (https://leetcode.com/problems/maximum-average-subarray-i/)

Given an array of integers `nums` and an integer `k`, find a contiguous subarray of length `k`
that has the maximum average value and return this value.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        :param nums: List[int] – the list of input integers
        :param k: int – the size of the sliding window
        :return: float – the maximum average of any contiguous subarray of length k

        Approach:
        1. Compute the sum of the first k elements as the initial window sum.
        2. Slide the window one step at a time:
           - Subtract the element leaving the window and add the new entering element.
           - Update max_sum if the new window sum is larger.
        3. Return max_sum divided by k.
        """
        n = len(nums)
        # Initial sum of the first window
        curr_sum = sum(nums[0:k])
        max_sum = curr_sum

        # Slide the window across the array
        for i in range(1, n):
            start = i
            end = i + k
            if end > n:
                break
            # Update running window sum
            curr_sum = curr_sum - nums[start - 1] + nums[end - 1]
            # Track the maximum window sum seen so far
            max_sum = max(curr_sum, max_sum)

        # Return the maximum average
        return max_sum / k
