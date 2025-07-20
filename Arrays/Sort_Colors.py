"""
LeetCode Problem “Sort Colors” (https://leetcode.com/problems/sort-colors/)

Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We use integers `0`, `1`, and `2` to represent the colors red, white, and blue respectively.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        :param nums: List[int] – the array of colors represented by 0 (red), 1 (white), and 2 (blue)
        :return: None – the list is modified in-place to group colors in the order 0, 1, 2

        Approach:
        - Use the Dutch National Flag algorithm with three pointers:
          low:  boundary for next 0 (red)
          mid:  current element under consideration
          high: boundary for next 2 (blue)
        - Traverse with mid from start to high:
          • if nums[mid] == 0, swap with nums[low], increment low and mid
          • if nums[mid] == 1, just increment mid
          • if nums[mid] == 2, swap with nums[high], decrement high
        """
        low, mid, high = 0, 0, len(nums) - 1

        # Process elements until mid passes high
        while mid <= high:
            if nums[mid] == 0:
                # Swap red (0) into the low region
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # White (1) is in correct region; move on
                mid += 1
            else:
                # Swap blue (2) into the high region
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
