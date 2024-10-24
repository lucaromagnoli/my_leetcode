"""
https://leetcode.com/problems/combination-sum-ii/
Title: Combination Sum II
No: 40
Difficulty: Medium
Category: Algorithms
Problem:
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
 
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

 
Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30


"""


class Solution:
    def combinationSum2(self, candidates: list[int], target_num: int):
        candidates.sort()
        solutions = []

        def inner(combo, start, target):
            if target == 0 and combo:
                solutions.append(combo[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                inner(combo, i + 1, target - candidates[i])
                combo.pop()

        inner([], 0, target_num)
        return solutions
