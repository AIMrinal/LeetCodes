"""
LeetCode Problem “Longest Common Prefix” (https://leetcode.com/problems/longest-common-prefix/)

Given an array of strings `strs`, return the longest common prefix among them.
If there is no common prefix, return an empty string "".

Time Complexity: O(m·n) where n = number of strings and m = length of the shortest string  
Space Complexity: O(m) for the prefix storage
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :param strs: List[str] – the list of input strings
        :return: str – the longest common prefix among all strings
        """
        k = 1  # length of prefix to test
        strs = sorted(strs, key=lambda x: len(x))  # sort so the shortest string is first
        key = strs[0]  # the shortest string serves as the maximum possible prefix
        st = ""  # stores the current longest common prefix

        while k <= len(key):
            for s in strs:
                if not s.startswith(key[0:k]):
                    # as soon as one string doesn't match, return the prefix found so far
                    return st
            # all strings shared this prefix of length k
            st = key[0:k]
            k += 1  # increase prefix length to test next

        return st
