"""
LeetCode Problem “Group Anagrams” (https://leetcode.com/problems/group-anagrams/)

Given an array of strings `strs`, group the anagrams together.
Return the answer in any order.

Time Complexity: O(n·k·log k), where n = len(strs) and k = max length of a string  
Space Complexity: O(n·k) for storing the grouped anagrams
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :param strs: List[str] – list of input strings
        :return: List[List[str]] – grouped anagrams

        Approach:
        1. Use a hash map (`tracker`) to map each word’s sorted-character signature to its anagram group.
        2. For each word, sort its characters to form the signature.
        3. Append the original word to the list at `tracker[signature]`, creating a new list if necessary.
        4. Return all lists of grouped anagrams.
        """
        tracker = {}  # Map sorted signature to list of anagrams
        for word in strs:
            sorted_word = "".join(sorted(word))  # signature: sorted characters
            if sorted_word in tracker:
                tracker[sorted_word].append(word)  # existing group
            else:
                tracker[sorted_word] = [word]      # new group
        return list(tracker.values())  # all anagram groups
