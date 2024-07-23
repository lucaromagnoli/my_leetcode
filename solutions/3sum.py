"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List


class Solution:

    def combinations(self, items, length):
        if length == 0:
            return [[]]
        if len(items) == 0:
            return []
        results = []
        for i in range(len(items)):
            for combo in self.combinations(items[i + 1 :], length - 1):
                results.append([items[i]] + combo)
        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        seen = set()
        for combo in self.combinations(nums, 3):
            key = "".join([str(c) for c in sorted(combo)])
            print(key)
            if key not in seen:
                seen.add(key)
                if sum(combo) == 0:
                    triplets.append(combo)

        return triplets


solution = Solution()
r = solution.threeSum([-1, 0, 1, 2, -1, -4])
print(r)
