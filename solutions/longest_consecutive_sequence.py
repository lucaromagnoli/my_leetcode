"""
https://leetcode.com/problems/longest-consecutive-sequence/
Title: Longest Consecutive Sequence
No: 128
Difficulty: Medium
Category: Algorithms
Problem:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
 
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 
Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109


"""


class Solution(object):
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        solutions = []
        cons = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                cons.append(nums[i])
            else:
                solutions.append(cons)
                cons = [nums[i]]
        solutions.append(cons)
        return len(max(solutions, key=len))
