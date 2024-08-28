"""
https://leetcode.com/problems/maximum-subarray/
Title: Maximum Subarray
No: 53
Difficulty: Medium
Category: Algorithms
Problem:
Given an integer array nums, find the subarray with the largest sum, and return its sum.
 
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_res = nums[0]
        res = 0

        for n in nums:
            if res < 0:
                res = n
            else:
                res += n
            if res > max_res:
                max_res = res
        return max_res
