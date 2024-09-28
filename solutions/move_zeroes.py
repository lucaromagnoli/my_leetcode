"""
https://leetcode.com/problems/move-zeroes/
Title: Move Zeroes
No: 283
Difficulty: Easy
Category: Algorithms
Problem:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
 
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]

 
Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

 
Follow up: Could you minimize the total number of operations done?
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        count_zeros = nums.count(0)
        found_zeros = 0
        while found_zeros != count_zeros:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                found_zeros += 1
                if i > 0:
                    i -= 1
            else:
                i += 1
        return nums
