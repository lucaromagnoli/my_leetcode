"""
https://leetcode.com/problems/sign-of-the-product-of-an-array/
Title: Sign of the Product of an Array
No: 1950
Difficulty: Easy
Category: Algorithms
Problem:
Implement a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.

You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).
 
Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

 
Constraints:

1 <= nums.length <= 1000
-100 <= nums[i] <= 100
import pytest
from solutions.sign_of_the_product_of_an_array import Solution

@pytest.mark.parametrize("nums, expected", [
    ([-1, -2, -3, -4, 3, 2, 1], 1),
    ([1, 5, 0, 2, -3], 0),
    ([-1, 1, -1, 1, -1], -1),
    ([1, 2, 3, 4, 5], 1),  # All positive numbers
    ([-1, -2, -3, -4, -5], -1),  # All negative numbers
    ([0, 0, 0], 0),  # All zeroes
    ([1, -1, 1, -1], 1),  # Mixed positive and negative numbers
    ([100, -100, 100, -100], 1),  # Large numbers
])
def array_sign_various_cases(nums, expected):
    solution = Solution()
    result = solution.arraySign(nums)
    assert result == expected

"""
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0

        mul = nums[0]
        for n in nums[1:]:
            mul *= n

        if mul > 0:
            return 1
        else:
            return -1
        