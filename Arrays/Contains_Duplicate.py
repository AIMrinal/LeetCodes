from typing import List

class Solution:
    """
    Solution to LeetCode Problem “Contains Duplicate” (https://leetcode.com/problems/contains-duplicate/).

    The method containsDuplicate checks whether any value appears at least twice in the list.
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determine if the input list contains any duplicates.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            bool: True if any integer appears more than once, False otherwise.

        Approach:
        ----------
        We iterate through the list, keeping track of all previously seen numbers
        in a hash set. For each number, we check set-membership in O(1) average time.
        If the number is already in the set, we immediately return True.
        If we finish the loop without finding any duplicate, we return False.

        Time Complexity:
            O(n), where n = len(nums). Each insert and membership check in the set
            takes amortized O(1), and we do one pass over nums.

        Space Complexity:
            O(n) in the worst case (when there are no duplicates), since we store
            each element in the set.
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
