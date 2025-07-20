"""
LeetCode Problem “Product of Array Except Self” (https://leetcode.com/problems/product-of-array-except-self/)

Given an integer array `nums` of length n, return an array `answer` where `answer[i]` is equal to the product of
all the elements of `nums` except `nums[i]`. The solution must run in O(n) time and cannot use division.

Time Complexity: O(n)
Space Complexity: O(1) extra space (excluding the output array)
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :param nums: List[int] – the input array of integers
        :return: List[int] – array where each element is the product of all other elements

        Approach:
        1. Use the `res` array to store running prefix products.
        2. First pass (left-to-right): fill `res[i]` with product of all elements before index i.
        3. Second pass (right-to-left): multiply `res[i]` by product of all elements after index i.
        """
        n = len(nums)
        res = [1] * n  # initialize result array with 1s

        # Build prefix products in res
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]  # update running prefix product

        # Multiply by suffix products in reverse order
        suffix = 1
        for j in range(n - 1, -1, -1):
            res[j] *= suffix  # combine with running suffix product
            suffix *= nums[j]  # update running suffix product

        return res
