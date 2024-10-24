"""
https://leetcode.com/problems/jump-game-ii/
Title: Jump Game II
No: 45
Difficulty: Medium
Category: Algorithms
Problem:
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
 
Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

 
Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].


"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = 0
        n = len(nums)
        end, far = 0, 0
        for i in range(n - 1):
            far = max(far, i + nums[i])
            print(
                f"Before if - i: {i} - far: {far} - end: {end} - smallest: {smallest}"
            )

            if i == end:
                smallest += 1
                end = far

            print(f"After if - i: {i} - far: {far} - end: {end} - smallest:{smallest}")

        return smallest