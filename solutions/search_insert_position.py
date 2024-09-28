"""
https://leetcode.com/problems/search-insert-position/
Title: Search Insert Position
No: 35
Difficulty: Easy
Category: Algorithms
Problem:
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def inner(l, r):
            if r - l == 1:
                if nums[l] >= target:
                    return l
                elif target > nums[r]:
                    return r + 1
                else:
                    return r

            mid = int((l + r) / 2)
            if target >= nums[mid]:
                return inner(mid, r)
            else:
                return inner(0, mid)

        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        return inner(0, len(nums) - 1)
