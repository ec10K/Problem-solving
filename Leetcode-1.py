"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR of a number with itself is 0
        # XOR of a number iwth 0 returns the number

         res = nums[0]

         for i in range(1,len(nums)):
            res = res ^nums[i]
         return res
        



