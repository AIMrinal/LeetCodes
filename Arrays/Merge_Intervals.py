"""
LeetCode Problem “Merge Intervals” (https://leetcode.com/problems/merge-intervals/)

Given a collection of intervals, merge all overlapping intervals and return an array
of the non-overlapping intervals that cover all the intervals in the input.

Time Complexity: O(n log n) due to sorting  
Space Complexity: O(n) for the result list
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        :param intervals: List[List[int]] – list of intervals [start, end]
        :return: List[List[int]] – merged, non-overlapping intervals

        Approach:
        1. Sort intervals by their start value.
        2. Initialize the result list with the first interval.
        3. Iterate through the remaining intervals:
           - If the current interval overlaps with the last in result (end ≥ next start),
             merge by updating the end to the max of both ends.
           - Otherwise, append the next interval as is.
        """
        # Sort intervals by start time
        intervals = sorted(intervals, key=lambda x: x[0])
        # Initialize result with the first interval
        res = [intervals[0]]
        j = 0  # index of the last interval in res

        # Process each interval and merge as needed
        for i in range(1, len(intervals)):
            curr = res[j]
            next_elem = intervals[i]
            # Check for overlap: current end >= next start
            if curr[1] >= next_elem[0]:
                # Merge by taking the min start and max end
                merged = [min(curr[0], next_elem[0]), max(curr[1], next_elem[1])]
                res[j] = merged
            else:
                # No overlap: append next interval
                res.append(next_elem)
                j += 1

        return res
