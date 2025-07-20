"""
Definition of Interval:
class Interval(object):
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

LeetCode Problem “Meeting Rooms” (https://leetcode.com/problems/meeting-rooms/)

Given a list of meeting intervals where intervals[i] = [start, end],
determine if a person could attend all meetings without any overlaps.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        :param intervals: List[Interval] – list of meeting intervals
        :return: bool – True if no intervals overlap, False otherwise

        Approach:
        1. If fewer than 2 intervals, cannot have overlaps → return True.
        2. Sort intervals by start time.
        3. Iterate through sorted intervals, comparing each start with previous end.
           If an overlap (start < previous end) is found, return False.
        4. Return True if no overlaps are detected.
        """
        if len(intervals) < 2:
            return True

        # Sort intervals by their start times
        intervals = sorted(intervals, key=lambda x: x.start)

        # Check for any overlapping adjacent intervals
        for i in range(1, len(intervals)):
            prev, curr = intervals[i - 1], intervals[i]
            if curr.start < prev.end:
                return False

        return True
