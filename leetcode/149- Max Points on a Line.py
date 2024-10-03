from collections import defaultdict
from fractions import Fraction
from typing import List, Tuple, Union


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Given a list of points as [x,y] it returns the max number of collinear points. 

        Args: 
            points: list of list of integers. 

        Returns
            int: max number of collinear points.

        """
        n = len(points)
        if n <= 2:
            return n

        line_to_points = defaultdict(set)
        for i in range(n):
            for j in range(i+1, n):
                line_spec = self.get_line_spec(points[i], points[j])
                line_to_points[line_spec].update([
                    tuple(points[i]),tuple(points[j])
                ])

        max_collinear_points = 0
        for points in line_to_points.values():
            max_collinear_points = max(max_collinear_points, len(points))

        return max_collinear_points

    
    def get_line_spec(
        self, 
        point1: List[int], 
        point2: List[int]
    ) -> Tuple[
        Union[Fraction, float], 
        Fraction
    ]:
        """
        Given 2 points, it returns the line specification for line y = ax+b going through the points. 

        Args:
            point1: list of ints, as [x1, y1]
            point2: list of ints, as [x2, y2]

        Returns 
            tuple of fractions (a, b) where a is the slope and b is the y-intercept.
            Edge case of x1 = x2, returns (float("inf"), x1).  
        """
        x1, y1 = point1
        x2, y2 = point2

        if x1 == x2:
            return (float("inf"), Fraction(x1))

        slope = Fraction(y1 - y2, x1 - x2)
        y_intercept = y1 - slope*x1

        return (slope, y_intercept)