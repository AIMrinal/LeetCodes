from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Return an array 'ans' of length 2 * len(nums) such that:
          ans[i] == nums[i] and ans[i + len(nums)] == nums[i]
        We achieve this by appending the first len(nums) elements onto the end of nums.
        """

        # 1. Record the original length of the list
        l = len(nums)

        # 2. For each index i in the range [0, l):
        #    append nums[i] (the original element) to the end of the list.
        #    After this loop, nums will have doubled in size,
        #    containing the original sequence followed by itself.
        for i in range(l):
            nums.append(nums[i])

        # 3. Return the now‑doubled list
        return nums
