"""
LeetCode Problem “Design HashSet” (https://leetcode.com/problems/design-hashset/)

Design a HashSet without using built-in hash table libraries.

Operations:
- add(key): Insert the value key into the HashSet.
- remove(key): Remove the value key in the HashSet. If key does not exist, do nothing.
- contains(key): Returns True if the key exists in the HashSet, False otherwise.

Time Complexity (worst-case, due to list operations):  
- add/remove/contains: O(n)  
Space Complexity: O(n)
"""

class MyHashSet:
    """
    A simple HashSet implementation using a Python list for storage.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Internal list to store keys
        self.keyset = []

    def add(self, key: int) -> None:
        """
        Inserts the key into the HashSet.
        
        :param key: int – the value to add
        """
        # Only add if the key is not already present
        if key not in self.keyset:
            self.keyset.append(key)

    def remove(self, key: int) -> None:
        """
        Removes the key from the HashSet if it exists.
        
        :param key: int – the value to remove
        """
        # If the key is present, remove it
        if key in self.keyset:
            self.keyset.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns True if the key exists in the HashSet, False otherwise.
        
        :param key: int – the value to check
        :return: bool
        """
        # Check membership in the internal list
        return key in self.keyset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
