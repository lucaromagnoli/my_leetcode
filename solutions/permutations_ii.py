"""
https://leetcode.com/problems/permutations-ii/
Title: Permutations II
No: 47
Difficulty: Medium
Category: Algorithms
Problem:
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
 
Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

 
Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

from collections import Counter


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = Counter(nums)
        solutions = []

        def backtrack(sol):
            if len(sol) == len(nums):
                solutions.append(sol[:])
                return

            for key in counter:
                if counter[key]:
                    sol.append(key)
                    counter[key] -= 1
                    backtrack(sol)
                    sol.pop()
                    counter[key] += 1

        backtrack([])
        return solutions
