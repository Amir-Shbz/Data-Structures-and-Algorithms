# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area 
# between two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). 
# The widest vertical area is the one with the maximum width.

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        
        x_points = [point[0] for point in points]

        x_points.sort()
        x_width = [x_points[x]-x_points[x-1] for x in range(1, len(x_points)) ]

        return max(x_width)
