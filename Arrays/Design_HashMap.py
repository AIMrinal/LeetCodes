"""
LeetCode Problem “Design HashMap” (https://leetcode.com/problems/design-hashmap/)

Design a HashMap without using built-in hash table libraries.

Operations:
- put(key, value): Insert a (key, value) pair into the HashMap. If the key already exists, update its value.
- get(key): Return the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- remove(key): Remove the mapping for the specified key if it exists.

Time Complexity: O(1) average for each operation  
Space Complexity: O(n)
"""

class MyHashMap:
    """
    A simple HashMap implementation using a Python dict for storage.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Internal dictionary to store key-value pairs
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        """
        Insert a (key, value) pair into the HashMap.
        If the key already exists, update its value.

        :param key: int – the key to insert or update
        :param value: int – the value to associate with the key
        """
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        """
        Return the value associated with the specified key, or -1 if no mapping exists.

        :param key: int – the key to look up
        :return: int – the value associated with the key, or -1 if not found
        """
        return self.hash_map.get(key, -1)

    def remove(self, key: int) -> None:
        """
        Remove the key and its associated value from the HashMap if it exists.

        :param key: int – the key to remove
        """
        self.hash_map.pop(key, None)
