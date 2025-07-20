from typing import List

class Solution:
    """
    Solution to LeetCode Problem “Valid Anagram” (https://leetcode.com/problems/valid-anagram/).

    The method isAnagram checks whether string t is an anagram of string s,
    i.e., both strings contain exactly the same characters with the same counts.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determine if t is an anagram of s.

        Args:
            s (str): The original string.
            t (str): The string to compare against s.

        Returns:
            bool: True if t is an anagram of s, False otherwise.

        Approach:
        ----------
        1. If lengths differ, they cannot be anagrams → return False.
        2. Build a set of unique characters from s.
        3. For each character in that set, compare its frequency in s vs. in t.
           If any mismatch, return False immediately.
        4. If all counts match, return True.

        Time Complexity:
            O(n · k) in the worst case, where n = length of s and k = number of unique characters.
            Each call to str.count scans the string (O(n)), and we do it for each distinct character.
            In practice this is O(n²) worst-case, but acceptable for moderate-length strings.

        Space Complexity:
            O(k) for storing the set of unique characters from s.
        """
        if len(s) != len(t):
            return False

        unique_chars = set(s)
        for ch in unique_chars:
            if s.count(ch) != t.count(ch):
                return False

        return True
