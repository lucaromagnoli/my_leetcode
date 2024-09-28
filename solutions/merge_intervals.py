"""
https://leetcode.com/problems/merge-intervals/
Title: Merge Intervals
No: 56
Difficulty: Medium
Category: Algorithms
Problem:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
 of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= start <= end <= 104


"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        def is_overlapping(x, y):
            return max(x[0], y[0]) <= min(x[1], y[1])

        if len(intervals) == 1:
            return intervals

        solutions = []
        intervals = sorted(intervals, key=lambda x: x[0])
        interval = intervals[0]

        for i in range(1, len(intervals)):
            next_interval = intervals[i]
            if is_overlapping(interval, next_interval):
                interval[1] = max(interval[1], next_interval[1])
            else:
                solutions.append(interval)
                interval = intervals[i]
            if i == len(intervals) - 1:
                solutions.append(interval)
        return solutions
